import numpy as np
from pandas import DataFrame, Series
from typing import Union, Optional, Tuple, List
from sklearn.base import RegressorMixin
from statsmodels.base.models import Model as StatsModel
from statsmodels.tsa.arima.model import ARIMA

class BenchmarkRegressor():
    '''
    Default Regression Model based on ARIMA (Auto-Regressive Integrated Moving 
    Averages). Aims to provide a basic compute-efficient time-series model to
    make predictions. (Aim to beat this model's prediction accuracy)
    '''
    def __init__(
            self,
            data: Union[DataFrame, Series],
            param: Tuple[int, int, int] = (5, 2, 0)
        ) -> None:

        self.model = ARIMA(data, order=param)
        self.model_fit = self.model.fit(data)
        self.residuals = DataFrame(self.model_fit.resid)


    def describe_residuals(self) -> DataFrame:
        return self.residuals.describe()
    

    def plot_residuals(self) -> None:
        self.residuals().plot()


    def cross_validate(
            self, 
            comparision_model: Optional[Union[
                    List,
                    RegressorMixin,
                    StatsModel
                ]]
        ) -> None:
        ...


    def predict(self) -> np.float64:
        ...
