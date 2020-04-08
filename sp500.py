from pandas_datareader import data as pdr 
from datetime import date
import yfinance as yf 
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt 

from data import data

#data.updateSP500()

sp500 = pd.read_csv('sp500.csv').to_numpy()

print(sp500[0:10])

#plt.plot(sp500)
#plt.show()