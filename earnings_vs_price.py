import yfinance as yf 
yf.pdr_override()
import matplotlib.pyplot as plt

def normalize (xs):
    maximum = max(xs)
    minimum = min(xs)

    xs = xs - minimum

    xs = xs / (maximum - minimum)

    return xs


#ticker = str(input("Ticker: "))
ticker = "AMZN"

company = yf.Ticker(ticker)

market_data = company.history(period='max')

price_data = market_data['Close']
price_data = normalize(price_data)
volume_data = market_data['Volume']


print(company.earnings)
#plt.plot(price_data)
#plt.show()