from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd

class data (object):

    @classmethod
    def updateSP500 (self):
        ticker= '^GSPC'
        today = date.today()
        start_date = "2000-01-01"
        data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
        close_price = data['Adj Close']
        close_price.to_csv('sp500.csv')