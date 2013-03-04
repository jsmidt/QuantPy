from pandas.io.data import DataReader
from pylab import legend, xlabel, ylabel, sqrt,ylim, cov, sqrt, mean, std
from numpy import array, zeros, matrix, ones, shape
from pandas import Series, DataFrame
from numpy.linalg import inv


# Portfolio class.
class Portfolio:
    def __init__(self, symbols, start = None, end = None, bench = '^GSPC'):

        # Make sure input is a list
        if type(symbols) != list: symbols = [symbols]

        # Create distionary to hold assets.
        self.asset = {} 

        # Retrieve assets from data source (IE. Yahoo)
        for symbol in symbols:
            try:
                self.asset[symbol] = \
                            DataReader(symbol, "yahoo", start=start, end=end)
            except:
                print "Asset "+str(symbol)+" not found!"

        # Get Benchmark asset.
        self.benchmark = DataReader(bench, "yahoo", start=start, end=end)
        self.benchmark['Return'] = self.benchmark['Adj Close'].diff()

        # Get returns, beta, alpha, and sharp ratio.
        for symbol in symbols:
            # Get returns.
            self.asset[symbol]['Return'] = \
                                self.asset[symbol]['Adj Close'].diff()
            # Get Beta.
            A = self.asset[symbol]['Return'].fillna(0)
            B = self.benchmark['Return'].fillna(0)
            self.asset[symbol]['Beta'] = cov(A,B)[0,1]/cov(A,B)[1,1]
            # Get Alpha
            self.asset[symbol]['Alpha'] = self.asset[symbol]['Return'] - \
                self.asset[symbol]['Beta']*self.benchmark['Return']

            # Get Sharpe Ratio
            tmp = self.asset[symbol]['Return']
            self.asset[symbol]['Sharpe'] = \
                sqrt(len(tmp))*mean(tmp.fillna(0))/std(tmp.fillna(0))
                                
    def nplot(self,symbol,color='b',nval=0):
        if symbol == 'bench':
            tmp = self.benchmark['Adj Close']
        else:
            tmp = self.asset[symbol]['Adj Close']
        tmp = tmp/tmp[nval]
        tmp.plot(color=color,label=symbol)
        legend(loc='best',shadow=True, fancybox=True)

    def betas(self):
        betas = []
        for symbol in self.asset.keys():
           betas.append(self.asset[symbol]['Beta'][0]) 
        return Series(betas,index=self.asset.keys())

    def returns(self):
        returns = []
        for symbol in self.asset.keys():
           returns.append(self.asset[symbol]['Return'].dropna()) 
        return Series(returns,index=self.asset.keys())

    def cov(self):
        tmp = self.returns()
       
        tmpl = [] 
        for symbol in tmp.keys():
            tmpl.append(tmp[symbol]) 
        return DataFrame(cov(array(tmpl)),index=tmp.keys(),columns=tmp.keys())

    def min_var_w_ret(self,ret):
        V = self.cov()
        suml = []
        for symbol in self.asset.keys():
            suml.append(self.returns()[symbol].sum())
        e = matrix(suml).T
        iV = matrix(inv(V))
        num = iV*e*ret
        denom = e.T*iV*e
        return Series(array(num/denom).flatten(),index=self.asset.keys())

    def ret_for_w(self,w):
        tmp = self.returns()
        i = 0
        tmpl = []
        for symbol in tmp.keys():
            tmpl.append(tmp[symbol]*w[i])
            i += 1
        return Series(tmpl,index=tmp.keys()).sum()

    def sharpe_w(self):
        V = self.cov()
        suml = []
        for symbol in self.asset.keys():
            suml.append(self.returns()[symbol].sum())
        e = matrix(suml).T
        iV = matrix(inv(V))
        num = iV*e
        denom = e.T*iV*e
        w = array(num/denom).flatten()
        return Series(w/abs(w.sum()),index=self.asset.keys())


