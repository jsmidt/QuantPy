import numpy as np
from pandas import DataFrame, Series
from typing import Union, Optional, Tuple, List
from sklearn.base import RegressorMixin
from statsmodels.base.models import Model as StatsModel
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

from exceptions import (
    ModelNotFittedError,
    ModelTypeNotSupportedError,
    DataTypeNotSupportedError
)

class BenchmarkRegressor():
    '''
    Default Regression Model based on ARIMA (Auto-Regressive Integrated Moving 
    Averages). Aims to provide a basic compute-efficient time-series model to
    make predictions. (Aim to beat this model's prediction accuracy)
    '''
    def __init__(
            self,
            data: Union[DataFrame, Series],
            param: Tuple[int, int, int] = (5, 2, 0),
            fit: bool = True,
            seasonal: bool = False,
            bias: Optional[float] = None
        ) -> None:
        self.data = data
        self.param = param
        self.model = ARIMA(data, order=param)
        self.bias = bias if bias else 0
        if fit:
            self.model_fit = self.model.fit(data + bias)
            self.residuals = DataFrame(self.model_fit.resid)


    def get_model(self) -> StatsModel:
        return self.model


    def get_summary(self) -> None:
        self.model.summary()


    def get_data(self) -> DataFrame:
        return self.data
    

    def get_params(self) -> Tuple:
        return self.params
    

    def fit(self):
        self.model_fit = self.model.fit(self.data + self.bias)
        self.residuals = DataFrame(self.model_fit.resid)


    def describe_residuals(self) -> DataFrame:
        if not self.residuals:
            raise ModelNotFittedError()
        return self.residuals.describe()
    

    def plot_residuals(self) -> None:
        if not self.residuals:
            raise ModelNotFittedError()
        self.residuals.plot()


    def cross_validate(
            self, 
            comparision_model: Optional[Union[
                    List,
                    RegressorMixin,
                    StatsModel
                ]]
        ) -> None:
        '''Validate based on data or compare to other models'''
        ...


    def predict(self, horizon: Union[int, Tuple] = None) -> np.float64:
        if not self.model_fit:
            raise ModelNotFittedError()
        if type(horizon) == int:
            return self.model_fit.forecast(steps=horizon)[0]
        elif type(horizon) == tuple:
            return self.model_fit.predict(start=horizon[0], end=horizon[1])
        else:
            return self.model_fit.forecast()[0]


class GARCH():
    '''
    Default GARCH (Generalized Auto-Regressive Conditional Heteroskedasticity)
    model to find forecasts based on changes of variances in a time-series. 
    Useful for Volatility.
    '''
    def __init__(
            self,
            data: Union[DataFrame, Series],
            p: int = 1,
            q: int = 1,
            fit: bool = True
        ) -> None:
        self.data = data
        self.p, self.q = p, q
        self.model = arch_model(data, mean='Zero', vol='GARCH', p=p, q=q)
        if fit:
            self.model_fit = self.model.fit()


    def get_model(self) -> arch_model:
        return self.model


    def get_data(self) -> DataFrame:
        return self.data
    

    def get_params(self) -> Tuple:
        return self.p, self.q
    

    def fit(self):
        self.model_fit = self.model.fit()


    def cross_validate(
            self,
            comparision_model: Optional[Union[
                    List,
                    RegressorMixin,
                    StatsModel
                ]]
        ) -> None:
        '''Validate based on data or compare to other models'''
        ...


    def predict(self, horizon: Union[DataFrame, Series]) -> Series:
        if not self.model_fit:
            raise ModelNotFittedError()
        return self.model_fit.forecast(horizon=horizon)


