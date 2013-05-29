import numpy as np
import pandas as pd


def sma(data, window):
    """Simple Moving Average, i.e. the average price of a security over a
    specific number of periods.

    'data' is a pandas Series or DataFrame of prices. A ValueError is raised
    if 'data' is of different data type.

    'window' is the number of observations.
    It must be a positive integer less than or equal to the length of the data.
    Otherwise a ValueError will be raised.
    """

    # todo: maybe add 'long' too?
    if not isinstance(window, int) or not 0 < window <= len(data):
        raise ValueError("'periods' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    return pd.rolling_mean(data, window)


def ema():
    pass
