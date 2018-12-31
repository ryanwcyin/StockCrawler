# StockCrawler

Download the data from yahoo and return a pandas Dataframe

## Getting Started

Clone the project and run `python setup.py install` to install the package.

### Prerequisites

`pandas` and `python3` are required

Install required packages:
```
pip install requirements.txt
```

### Quick Start

```
from StockCrawler.StockCrawler import load_yahoo_quote
START_DATE = '20160101' # should in YYYYMMDD format
END_DATE = '20180101'
TICKER = 'AAPL'
df = load_yahoo_quote(TICKER,START_DATE,END_DATE)
```

## Versioning

Last update: 3/5/2018

## Authors

* **Ryan Wong**

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ryanwcyin/StockCrawler/blob/master/LICENSE) file for details

## Acknowledgments

* This project is an enhanced version from [c0redumb/yahoo_quote_download](https://github.com/c0redumb/yahoo_quote_download)
