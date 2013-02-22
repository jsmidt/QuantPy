from pandas.io.data import DataReader
from pylab import legend, xlabel, ylabel, sqrt,ylim

# Stock class.
class Stock:
    def __init__(self, symbol, start = None, end = None):
        self.symbol = symbol
        self.data = DataReader(symbol, "yahoo", start=start, end=end)

    def plot(self,logy=True,color='b'):
        self.data['Close'].plot(logy=logy,color=color,label=self.symbol)
        ylabel('Price')
        ylim(1e1,1e3)
        legend(loc='best',shadow=True, fancybox=True)

    def sharpe(self):
        return sqrt(self.data['Adj Close'].size-1.0) * \
               self.data['Adj Close'].diff().mean() /  \
               self.data['Adj Close'].diff().std()
