from sklearn import linear_model

import numpy as np

import pandas as pd

import matplotlib

import matplotlib.pyplot as plt

from sklearn import datasets


boston_house_prices = datasets.load_boston()

data_frame = pd.DataFrame(boston_house_prices.data)

data_frame.columns = boston_house_prices.feature_names

data_frame['Price'] = boston_house_prices.target

linear = linear_model.LinearRegression()

linear.fit(X = pd.DataFrame(data_frame["RM"]), y = data_frame["Price"])

prediction = linear.predict(X = pd.DataFrame(data_frame["RM"]))

print(linear.intercept_)

print(linear.coef_)

