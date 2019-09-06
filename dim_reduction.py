#!/usr/bin/env python3
from functions_script import mean
import matplotlib.pyplot as plt
import numpy as np


def covariance_matrix():
    pass


def sample_cov(x, y):
    mx = mean(x)
    my = mean(y)
    aggregate = 0.
    for xi, yi in zip(x, y):
        aggregate += (xi - mx)*(yi - my)
    return aggregate/(len(x)-1)


def trace(matrix):
    s = 0.0
    for i, element in enumerate(matrix):
        s += matrix[i][i]
    return s


def main():

    x = (12, 30, 15, 24, 14, 18, 28, 26, 19, 27)
    y = (20, 60, 27, 50, 21, 30, 61, 54, 32, 57)

    print('Sample Cov:', sample_cov(x, y))

    something = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

    print(trace(something))


if __name__ == '__main__':
    main()
