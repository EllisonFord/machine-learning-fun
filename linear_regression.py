#!/usr/bin/env python3
import matplotlib.pyplot as plt
from functions_script import noisy_sine
import numpy as np


def y(X, W):
    WT = np.transpose(W)
    return np.product(WT, X)


def main(*args, **kwargs):

    X = noisy_sine(samples=10, precision=10)

    # Normally MxN where M is the rows, N is the cols
    N = len(X)  # Rows
    D = 1  # Columns

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
