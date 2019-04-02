#!/usr/bin/env python3
import matplotlib.pyplot as plt
from math import sin, pi, exp
import numpy as np
import random


def noisy_sine(samples, precision):
    X = []  # Targets Z
    for x_i in range(samples+1):
        X.append(sin((2*pi*x_i)/samples) + random.gauss(0, 1/precision))
    plt.scatter(range(samples+1), X)
    plt.title('Generated Noisy Sinusoid')
    plt.show()
    return X


def sigmoid(x):
    return 1 / (1 + exp(-x))


def polynomial():
    pass


def gaussian(alpha, x, sigma):
    alpha*exp(-(x*x/sigma*sigma))


def y(X, W):
    WT = np.transpose(W)
    return np.product(WT, X)


def main():

    X = noisy_sine(samples=10, precision=10)

    D = len(X)  # Rows
    N = 1  # Columns



    """ # Pseudo Inverse calculation and multiplication
    X = np.random.randn(2, 3)
    for element in X:
        print(element)
    print()

    PX = np.linalg.pinv(X)
    for element in PX:
        print(element)
    print()

    new = np.dot(X, PX)
    for element in new:
        print(element)
    print()
    """

if __name__ == '__main__':
    main()
