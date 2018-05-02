import unittest
import pandas as pd
from StockCrawler.StockCrawler import load_yahoo_quote


class TestStockCralwer(unittest.TestCase):

    _result = None

    @classmethod
    def setUpClass(cls):
        global _result
        _result = load_yahoo_quote('AAPL', '20170101', '20180101')

    def test_load_yahoo_quote_return_df(self):
        global _result
        self.assertTrue(isinstance(_result, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()
