#%%
from math import degrees
from numpy.core.fromnumeric import size
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import PolynomialFeatures

# %%
datas = pd.read_csv('./out/WD.csv')
datas

# %%
datas = datas.values
X = datas[:,6:7]
y = datas[:,10:11]

# %%
X

# %%
y = y.reshape(y.size)
X = np.sort(X,axis=0)
y = np.sort(y)

# %%
poly_reg = PolynomialFeatures(degree=2)

# %%
X = poly_reg.fit_transform(X)
X

# %%
liner = LinearRegression()
liner.fit(X,y)

# %%
plt.plot(X,liner.predict(X))
plt.plot(X,y,'o')

# %%


# %%
