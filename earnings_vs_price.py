import yfinance as yf 
yf.pdr_override()
from pandas_datareader import data as pdr 
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt
import pandas as pd
import datetime

api_key = "39909968fea57578dfad64131ffbc423"
#ticker = str(input("Ticker: "))
ticker = "V"
end_date = "2021-01-01"
start_date = "1980-01-01"

def normalize (xs):
    maximum = max(xs)
    xs = xs / maximum
    return xs

# Stock price data
price_data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)['Adj Close']
price_data = normalize(price_data)

# Earnings evolution
ebitda = fa.income_statement(ticker, api_key, period="year").loc['operatingIncome']
ebitda = normalize(ebitda)
index = list(ebitda.index.values)
earnings = ebitda.values
index = list(map(lambda d: datetime.datetime.strptime(d, "%Y").replace(day = 31, month = 12), index))
ebitda = pd.DataFrame(data=earnings, index=index, columns=['EBITDA'])

'''
# Market cap evolution
market_cap = fa.enterprise(ticker, api_key=api_key, period="year").loc['marketCapitalization']
index = list(market_cap.index.values)
values = market_cap.values
index = list(map(lambda d: datetime.datetime.strptime(d, "%Y").replace(day = 31, month = 12), index))
market_cap = pd.DataFrame(data=values, index = index, columns = ['Market cap'])
print(market_cap)
'''

pe_ratio = fa.financial_ratios(ticker, api_key, period='year').loc['priceEarningsRatio']
print(pe_ratio)
index = list(pe_ratio.index.values)
values = pe_ratio.values
index = list(map(lambda d: datetime.datetime.strptime(d, "%Y").replace(day = 31, month = 12), index))
pe_ratio = pd.DataFrame(data=values, index=index, columns=['PE Ratio'])

fig, axs = plt.subplots(2, sharex=True)

axs[0].plot(price_data, label = "Price")
axs[0].plot(ebitda, label = "EBITDA")
axs[0].set_title("{} - Price vs EBITDA".format(ticker))
axs[0].set(Ylabel="Fraction of maximum")
axs[0].legend()

axs[1].plot(pe_ratio)
axs[1].set_title("{} - PE Ratio".format(ticker))
axs[1].set_ylim(0,50)

fig.tight_layout(pad=2)

plt.savefig("{} - price vs earnings".format(ticker))
plt.show()