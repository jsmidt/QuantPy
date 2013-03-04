from pylab import *
import portfolio

P = portfolio.Portfolio(['IBM','GOOG','MSFT','AAPL','INTC'])

w = P.min_var_w_ret(1000)
aa = P.ret_for_w(w)
cumsum(aa).plot()

bb = P.ret_for_w(ones(5))
cumsum(bb).plot()
show()

