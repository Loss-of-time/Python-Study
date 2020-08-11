# +--------------------------------------------------------------+
# | Size         | 1.73 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 691 bytes                                     |
# |--------------------------------------------------------------|
# | Created      | August 11th 2020, 12:23:37                    |
# |--------------------------------------------------------------|
# | Changed      | August 11th 2020, 13:07:20                    |
# +--------------------------------------------------------------+


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

def getData(path):
    data = pd.read_csv(path)
    data = data.values
    x = data[:, 1:5]
    y = data[:, 5]
    poly = PolynomialFeatures(6)
    X = poly.fit_transform(x)
    # print(X)
    return X,y

def fitModle(xTrain,yTrain):
    clf = Ridge(alpha=1.0,fit_intercept=True)
    clf.fit(xTrain, yTrain)
    score = cross_val_score(clf,xTrain,yTrain,cv=4)
    print(score)
    return clf


def showModle(modle,xTest,yTest):
    start = 100
    num = 200
    plt.plot(yTest[start:start+num],label='real')
    plt.plot(modle.predict(xTest[start:num+start]),label='predict')
    plt.legend(loc='upper left') # 设置图例位置
    plt.show()


def main():
    x,y =getData(r'lib\data\岭回归.csv')
    xTrain,xTest,yTrain,yTest = train_test_split(x,y)
    clf = fitModle(xTrain,yTrain)
    showModle(clf,xTest,yTest)


if __name__ == "__main__":
    main()
