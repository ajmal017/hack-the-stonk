from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 


#data.updateSP500()

ticker_sp = '^GSPC'
ticker_dow = '^DJI'
ticker_nasdq = '^IXIC'
ticker_dax = '^GDAXI'
ticker_nikkei = '^N225'
ticker_ibex = '^IBEX'
ticker_gold = 'GC=F'
ticker_silver = 'SI=F'
ticker_oil = 'CL=F'

today = date.today()
start_date = "2000-01-01"

def getNormalisedData (ticker):
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    adj_close = data['Adj Close']
    max_price = max(adj_close)
    normalisedData = adj_close/max_price
    return normalisedData


plt.plot(getNormalisedData(ticker_sp))
#plt.plot(getNormalisedData(ticker_dow))
#plt.plot(prices_nasdaq/max_price_nasdaq)
#plt.plot(getNormalisedData(ticker_dax))
#plt.plot(getNormalisedData(ticker_nikkei))
#plt.plot(getNormalisedData(ticker_ibex))
#plt.plot(getNormalisedData(ticker_gold))
#plt.plot(getNormalisedData(ticker_silver))
plt.plot(getNormalisedData(ticker_oil))

plt.legend(['SP500', 'OIL'])

print(getNormalisedData(ticker_oil))
plt.show()