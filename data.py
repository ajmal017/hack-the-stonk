from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 
import math
import quandl

ticker_sp = '^GSPC'
ticker_gold = 'GC=F'
ticker_oil = 'CL=F'
ticker_dax = '^GDAXI'
ticker_nikkei = '^N225'
ticker_ftse = '^FTSE'
ticker_shanghai = '000001.SS'

auth_tok = "Nv1rJgRR7u88iz_dg7Y6"

end_date = "2020-05-1"
start_date = "2000-01-01"


def getGOLDData ():
    # Contains price and volume
    data = quandl.get("CHRIS/CME_GC1", trim_start = start_date, trim_end = end_date, authtoken=auth_tok)
    data = data[['Last', 'Volume']]
    data.columns = ["GOLD Adj Close", "GOLD Volume"]
    return data.dropna()

def getSPData():
    # Contains price and volume
    data = pdr.get_data_yahoo(ticker_sp, start=start_date, end=end_date)
    data = data[data.columns[4:6]] # Takes only Adj. Close and Volume
    data.columns = ["SP500 Adj Close",  "SP500 Volume"]
    return data

def getDAXData():
    # Contains price and volume
    data = pdr.get_data_yahoo(ticker_dax, start=start_date, end=end_date)
    data = data[data.columns[4:6]] # Takes only Adj. Close and Volume
    data.columns = ["DAX Adj Close",  "DAX Volume"]
    return data


def getOILData():
    # Contains price and volume

    data = quandl.get("CHRIS/CME_CL1", trim_start = start_date, trim_end = end_date, authtoken=auth_tok)
    data = data[["Last", "Volume"]]
    data.columns=["OIL Adj Close", "OIL Volume"]
    return data.dropna()

#TODO: Increase timeframe
def getNIKKEIData():
    # Contains only price
    data = pdr.get_data_yahoo(ticker_nikkei, start=start_date, end=end_date)
    data = data[data.columns[4:5]] # Takes only Adj. Close 
    data.columns = ["NIKKEI Adj Close"]
    return data


def getFTSEData():
    data = pdr.get_data_yahoo(ticker_ftse, start=start_date, end=end_date)
    data = data[data.columns[4:6]] # Takes only Adj. Close and Volume
    data.columns = ["FTSE Adj Close",  "FTSE Volume"]
    return data

def getSHANGHAIData():
    data = pdr.get_data_yahoo(ticker_shanghai, start=start_date, end=end_date)
    data = data[data.columns[4:5]] # Takes only Adj. Close and Volume
    data.columns = ["SHANGHAI Adj Close"]
    return data

def checkData (data):
    counter = 0
    for index, row in data.iterrows():
        for item in row:
            if (math.isnan(item)):
                counter += 1
                break
    return counter

def normalizeData(data):
    for column in data:
        maxValue = max(data[column])
        data[column] = data[column] / maxValue

def combineData():
    allData = [getSPData(), getGOLDData(), getDAXData(), getOILData(), getNIKKEIData(), getSHANGHAIData(), getFTSEData()]
    mergedData = pd.concat(allData, axis = 1)
    print("REMOVED: {} DATA POINTS".format(checkData(mergedData)))
    cleanData = mergedData.dropna()
    normalizeData(cleanData)
    return cleanData

print(combineData())

