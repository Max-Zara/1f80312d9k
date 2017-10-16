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

print("Mean Squared Error: %.2f"
% mean_squared_error(diabetes_y_test,diabetes_y_pred))

print('Variance score: %.2f' % r2_score(diabetes_y_test,diabetes_y_pred))

plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas

from mpl_toolkits.mplot3d import Axes3D

from statsmodels.formula.api import ols

from statsmodels.stats.anova import anova_lm

#seq - x is a linear line from -5 to 5 with 21 series in between
x = np.linspace(-5,5,21)

X,Y = np.meshgrid(x,x)

np.random.seed(1)

Z = -5 + 3*X -0.5*Y + 8 * np.random.normal(size = X.shape)

fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X,Y,Z, cmap = plt.cm.coolwarm,
                       rstride=1, cstride = 1)

ax.view_init(20, -120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

X = X.flatten()
Y = Y.flatten()
Z = Z.flatten()

data = pandas.DataFrame({'x':X,'y':Y,'z':Z})

model = ols("z ~ x + y",data).fit()

print(model.summary())

