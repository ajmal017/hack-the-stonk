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
ticker_nasdq = '^IXIC'
ticker_dax = '^GDAXI'
ticker_nikkei = '^N225'
ticker_ibex = '^IBEX'

today = date.today()
start_date = "2000-01-01"

data_sp = pdr.get_data_yahoo(ticker_sp, start=start_date, end=today)
data_dow = pdr.get_data_yahoo(ticker_dow, start=start_date, end=today)
data_nasdaq = pdr.get_data_yahoo(ticker_nasdq, start=start_date, end=today)
data_dax = pdr.get_data_yahoo(ticker_dax, start=start_date, end=today)
data_nikkei = pdr.get_data_yahoo(ticker_nikkei, start=start_date, end=today)
data_ibex = pdr.get_data_yahoo(ticker_ibex, start=start_date, end=today)

prices_sp = data_sp['Adj Close']
prices_dow = data_dow['Adj Close']
prices_nasdaq = data_nasdaq['Adj Close']
prices_dax = data_dax['Adj Close']
prices_nikkei = data_nikkei['Adj Close']
prices_ibex = data_ibex['Adj Close']

max_price_sp = max(prices_sp)
max_price_dow = max(prices_dow)
max_price_nasdaq = max(prices_nasdaq)
max_price_dax = max(prices_dax)
max_price_nikkei = max(prices_nikkei)
max_price_ibex = max(prices_ibex)

#plt.plot(prices_sp/max_price_sp)
plt.plot(prices_dow/max_price_dow)
#plt.plot(prices_nasdaq/max_price_nasdaq)
plt.plot(prices_dax/max_price_dax)
plt.plot(prices_nikkei/max_price_nikkei)
plt.plot(prices_ibex/max_price_ibex)

plt.legend(['DOW JONES', 'DAX', 'NIKKEI', 'IBEX'])


plt.show()