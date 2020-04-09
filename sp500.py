from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 

from data import data

#data.updateSP500()

ticker_sp = '^GSPC'
ticker_dow = '^DJI'

today = date.today()
start_date = "2000-01-01"

data_sp = pdr.get_data_yahoo(ticker_sp, start=start_date, end=today)
data_dow = pdr.get_data_yahoo(ticker_dow, start=start_date, end=today)

prices_sp = data_sp['Adj Close']
prices_dow = data_dow['Adj Close']

max_price_sp = max(prices_sp)
max_price_dow = max(prices_dow)

plt.plot(prices_sp/max_price_sp)
plt.plot(prices_dow/max_price_dow)

plt.legend(['S&P500', 'DOW JONES'])

plt.show()