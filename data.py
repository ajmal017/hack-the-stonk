from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 
import math
import quandl
import numpy as np

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
    data = data[data.columns[4:6]] 
    data.columns = ["SP500 Adj Close",  "SP500 Volume"]
    return data

def getDAXData():
    # Contains price and volume
    data = pdr.get_data_yahoo(ticker_dax, start=start_date, end=end_date)
    data = data[data.columns[4:6]]
    data.columns = ["DAX Adj Close",  "DAX Volume"]
    return data


def getOILData():
    # Contains price and volume
    data = quandl.get("CHRIS/CME_CL1", trim_start = start_date, trim_end = end_date, authtoken=auth_tok)
    data = data[["Last", "Volume"]]
    data.columns=["OIL Adj Close", "OIL Volume"]
    return data.dropna()


def getNIKKEIData():
    # Contains only price
    data = pdr.get_data_yahoo(ticker_nikkei, start=start_date, end=end_date)
    data = data[data.columns[4:5]] 
    data.columns = ["NIKKEI Adj Close"]
    return data


def getFTSEData():
    # Contains price and volume
    data = pdr.get_data_yahoo(ticker_ftse, start=start_date, end=end_date)
    data = data[data.columns[4:6]] 
    data.columns = ["FTSE Adj Close",  "FTSE Volume"]
    return data

def getSHANGHAIData():
    # Contains only price
    data = pdr.get_data_yahoo(ticker_shanghai, start=start_date, end=end_date)
    data = data[data.columns[4:5]] 
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

data = combineData()

print(data)

day_counter = 0

# Size of prediction
prediction_size = 5

# Size of available data.
data_size = len(data) - prediction_size

# Size of data alocated to training
size_training = int(0.75*data_size)

# Size of data alocated to testing
size_testing = data_size - size_training

# Number of data elements in a single day
size_day = 12 

# Number of days in the past
size_historical = 15

x_train = np.zeros((size_training, size_historical, size_day))
x_test  = np.zeros((size_testing, size_historical, size_day))

for index, row in data.iterrows():

    if (day_counter < len(x_train)):

        for i in range (size_historical):
            for j in range (size_day):
                x_train[day_counter][i][j] = data.iloc[day_counter+i][j]
            
    #else:
        # Append data to x_test
    day_counter += 1
    print("{}% completed".format(int(100 * day_counter/data_size)), end = '\r')

print(x_train)


'''
1 - Split data into training and testing
2 - Prepare input and output data
'''

