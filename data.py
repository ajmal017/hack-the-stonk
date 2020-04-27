from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 
import math

ticker_sp = '^GSPC'
ticker_gold = 'GC=F'
ticker_oil = 'CL=F'
ticker_dax = '^GDAXI'
ticker_nikkei = '^N225'

today = date.today()
start_date = "1950-01-01"

def getRawData (ticker):
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    return data

def getPriceAndVolume (ticker, name):
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    data = data[data.columns[4:6]] # Takes only Adj. Close and Volume
    data.columns = [name + ' Adj Close', name +' Volume']
    return data

def getPrice (ticker, name):
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    data = data[data.columns[4:5]] # Takes only Adj. Close and Volume
    data.columns = [name + ' Adj Close']
    return data

def checkData (data):
    for index, row in data.iterrows():
        for item in row:
            if (math.isnan(item)):
                return False
    return True
            
def buildDataSet():
    sp = getPriceAndVolume(ticker_sp, "SP500")
    gold = getPrice(ticker_gold, "Gold")
    oil = getPrice(ticker_oil, "USA Oil")
    dax = getPriceAndVolume(ticker_dax, "DAX")
    nikkei = getPriceAndVolume(ticker_nikkei, "NIKKEI")



sp = getPriceAndVolume(ticker_sp, "SP500")
gold = getPrice(ticker_gold, "Gold")
oil = getPrice(ticker_oil, "USA Oil")
dax = getPriceAndVolume(ticker_dax, "DAX")
nikkei = getPriceAndVolume(ticker_nikkei, "NIKKEI")
print(nikkei)