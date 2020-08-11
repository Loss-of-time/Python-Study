# %%
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# %%
data = load_iris()
data

# %%
x = data.data
y = data.target

# %%
pca = PCA(n_components=2)

# %%
reduce_X = pca.fit_transform(x)
reduce_X

# %%
rX = []
rY = []
bX = []
bY = []
gX = []
gY = []


# %%
for i in range(len(reduce_X)):
    if y[i]==0:
        rX.append(reduce_X[i][0])
        rY.append(reduce_X[i][1])
    if y[i]==1:
        bX.append(reduce_X[i][0])
        bY.append(reduce_X[i][1])
    if y[i]==2:
        gX.append(reduce_X[i][0])
        gY.append(reduce_X[i][1])

# %%
plt.scatter(rX,rY,c='r',marker='x')
plt.scatter(bX,bY,c='b',marker='D')
plt.scatter(gX,gY,c='g',marker='.')

# %%
