#print(__doc__)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


diabetes = datasets.load_diabetes()
diab = pd.DataFrame(diabetes.data)

diabetes_X = diabetes.data[:, np.newaxis,2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]


regr = linear_model.LinearRegression()

regr.fit(diabetes_X_train,diabetes_y_train)

diabetes_y_pred = regr.predict(diabetes_X_test)

print('Coefficients: \n',regr.coef_)
