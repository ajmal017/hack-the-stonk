import yfinance as yf 
yf.pdr_override()
from pandas_datareader import data as pdr 
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt
import pandas as pd
import datetime

api_key = "39909968fea57578dfad64131ffbc423"
#ticker = str(input("Ticker: "))
ticker = "AAPL"
end_date = "2021-01-01"
start_date = "1980-01-01"

def normalize (xs):
    maximum = max(xs)
    xs = xs / maximum
    '''
    minimum = min(xs)

    xs = xs - minimum

    xs = xs / (maximum - minimum)
    '''
    return xs

company = yf.Ticker(ticker)

market_data = company.history(period='max')

price_data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)['Adj Close']
price_data = normalize(price_data)


ebitda = fa.income_statement(ticker, api_key, period="year").loc['operatingIncome']
print(ebitda)
ebitda = normalize(ebitda)
index = list(ebitda.index.values)
earnings = ebitda.values
index = list(map(lambda d: datetime.datetime.strptime(d, "%Y").replace(day = 31, month = 12), index))
ebitda = pd.DataFrame(data=earnings, index=index, columns=['EBITDA'])

# TODO: Dates are set by default to start at day 1 even though there is no date data


plt.plot(price_data, label = "Price")
plt.plot(ebitda, label = "EBITDA")
plt.title("{} - Price vs EBITDA".format(ticker))
plt.xlabel("Time")
plt.ylabel("Fraction of maximum")
plt.legend()
plt.show()
