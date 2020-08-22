import yfinance as yf 
yf.pdr_override()
from pandas_datareader import data as pdr 
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt

api_key = "39909968fea57578dfad64131ffbc423"
#ticker = str(input("Ticker: "))
ticker = "AMZN"
end_date = "2021-01-01"
start_date = "1980-01-01"

def normalize (xs):
    maximum = max(xs)
    minimum = min(xs)

    xs = xs - minimum

    xs = xs / (maximum - minimum)

    return xs

company = yf.Ticker(ticker)

market_data = company.history(period='max')

price_data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)['Adj Close']
#price_data = normalize(price_data)
print(price_data.shape)

ebitda = fa.income_statement(ticker, api_key, period="quarter").loc['operatingIncome']
ebitda = normalize(ebitda)
ebitda = ebitda.iloc[::-1]

print(type(ebitda.index.values[0]))

'''
plt.plot(price_data, label = "Price")
plt.plot(ebitda, label = "EBITDA")
plt.ylabel("Time")
plt.legend()
plt.show()
'''