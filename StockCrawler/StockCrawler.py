import urllib.request, urllib.parse, urllib.error
import pandas as pd
import time
from io import StringIO
pd.set_option('display.width', 1000)

# Build the cookie handler
cookier = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookier)
urllib.request.install_opener(opener)

# Cookie and corresponding crumb
_cookie = None
_crumb = None

# Headers to fake a user agent
_headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


def _get_cookie_crumb():
    '''
    This function perform a query and extract the matching cookie and crumb.
    '''

    # Perform a Yahoo financial lookup on SP500
    req = urllib.request.Request('https://finance.yahoo.com/quote/AAPL', headers=_headers)
    f = urllib.request.urlopen(req)
    alines = f.read().decode('utf-8')

    # Extract the crumb from the response
    global _crumb
    target_crumbstore = '"CrumbStore":{"crumb":"'
    begin = alines.find(target_crumbstore)
    end = alines.find('"},', begin + len(target_crumbstore))
    crumb = alines[begin + len(target_crumbstore):end]
    _crumb = crumb.encode("UTF-8").decode("unicode_escape")
    # Extract the cookie from cookiejar
    global cookier, _cookie
    for c in cookier.cookiejar:
        if c.domain != '.yahoo.com':
            continue
        if c.name != 'B':
            continue
        _cookie = c.value


def load_yahoo_quote(ticker, begindate, enddate, info='quote'):
    '''
    This function load the corresponding history/divident/split from Yahoo.
    begindate & enddate in yyyyddmm format
    '''
    # Check to make sure that the cookie and crumb has been loaded
    global _cookie, _crumb
    if _cookie == None or _crumb == None:
        _get_cookie_crumb()

    # Prepare the parameters and the URL
    tb = time.mktime((int(begindate[0:4]), int(begindate[4:6]), int(begindate[6:8]), 4, 0, 0, 0, 0, 0))
    te = time.mktime((int(enddate[0:4]), int(enddate[4:6]), int(enddate[6:8]), 18, 0, 0, 0, 0, 0))

    param = dict()
    param['period1'] = int(tb)
    param['period2'] = int(te)
    param['interval'] = '1d'
    if info == 'quote':
        param['events'] = 'history'
    elif info == 'dividend':
        param['events'] = 'div'
    elif info == 'split':
        param['events'] = 'split'
    param['crumb'] = _crumb
    params = urllib.parse.urlencode(param)
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?{}'.format(ticker, params)
    req = urllib.request.Request(url, headers=_headers)

    # Perform the query
    # There is no need to enter the cookie here, as it is automatically handled by opener
    f = urllib.request.urlopen(req)
    alines = f.read().decode('utf-8')

    df = pd.read_csv(StringIO(alines))

    return df
