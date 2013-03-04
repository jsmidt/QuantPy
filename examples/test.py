from pylab import *
import portfolio

syms = ['IBM','GOOG','MSFT','AAPL','INTC']
cols = ['b','r','g','k','m','y']

P = portfolio.Portfolio(syms)

for sym,col in zip(syms,cols):
    P.nplot(sym,col)
show()
