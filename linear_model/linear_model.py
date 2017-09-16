"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 13 September, 2017 @ 12:24 AM.
  Copyright (c) 2017. Victor. All rights reserved.
"""

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, learning_rate=1e-3):
        self.learning_rate = learning_rate
        self.W = np.array([])
        self.b = np.array([])

    def fit(self, X, y, num_iter=10000):
        weight_shape = [X.shape[1], y.shape[1]]
        bias_shape = [y.shape[1]]
        self.W = np.random.random(weight_shape)
        self.b = np.random.random(bias_shape)
        for _ in range(num_iter):
            self.__gradientDescent(X, y)

    def predict(self, x):
        return np.dot(x, self.W) + self.b

    def error(self, X, y):
        y_hat = np.array([self.predict(x) for x in X])
        total_error = np.square(np.subtract(y, y_hat))
        return np.mean(total_error)

    """
    def score(self, X, y, sample_weight=None):
        from sklearn.metrics import accuracy_score
        return accuracy_score(y, self.predict(X), sample_weight=sample_weight)
    """

    def __gradientDescent(self, X, y):
        m = len(X)
        w_gradient = 0
        b_gradient = 0
        for i, _ in enumerate(X):
            x = X[i]
            y_ = y[i]
            w_gradient += (self.predict(x) - y_) / m
            b_gradient += (self.predict(x) - y_) / m
        self.W = self.W - (self.learning_rate * w_gradient)
        self.b = self.b - (self.learning_rate * b_gradient)


if __name__ == '__main__':
    X, y = np.genfromtxt('../datasets/data.csv', delimiter=',', unpack=True)
    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # !- Using the model
    clf = LinearRegression()
    clf.fit(X_train, y_train)

    # !- Evaluating the accuracy
    err = clf.error(X_test, y_test)
    print('Classification error = {:.02f}'.format(err))

    # !- Visualizing the model
    # plt.scatter(X[:, 0], y)
    # plt.show()
