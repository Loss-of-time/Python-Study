# +--------------------------------------------------------------+
# | Size         | 2.45 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 825 bytes                                     |
# |--------------------------------------------------------------|
# | Created      | August 4th 2020, 09:27:23                     |
# |--------------------------------------------------------------|
# | Changed      | August 5th 2020, 09:32:41                     |
# +--------------------------------------------------------------+

import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def knn():
    # 导入数据
    iris = load_iris()
    print(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, random_state=666)
    # 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 测试
    y_pridect = estimator.predict(x_test)
    score = estimator.score(x_test, y_test)
    print(x_test)
    print(score)


def bayes():
    #
    news = fetch_20newsgroups(subset='all')
    xTrain, xTest, yTrain, yTest = train_test_split(news.data, news.target)
    #
    tf = TfidfVectorizer()
    xTrain = tf.fit_transform(xTrain)
    xTest = tf.transform(xTest)
    #
    em = MultinomialNB()
    em.fit(xTrain, yTrain)
    #
    score = em.score(xTest, yTest)
    print(score)


def decisionTrees():
    #
    iris = load_iris()
    xTrain, xTest, yTrain, yTest = train_test_split(
        iris.data, iris.target, random_state=666)
    #
    em = DecisionTreeClassifier(criterion='entropy')
    em.fit(xTrain, yTrain)
    #
    score = em.score(xTest, yTest)
    print(score)
    # 可视化决策树
    export_graphviz(em, out_file='out/irisTree.dot',
                    feature_names=iris.feature_names)


if __name__ == "__main__":
    knn()
    # bayes()
    # decisionTrees()
