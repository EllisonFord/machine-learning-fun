#!/usr/bin/env python3
from functions_script import mean, plt
import numpy as np


def covariance_matrix():
    pass


def sample_cov(x: list, y: list) -> float:
    mx = mean(x)
    my = mean(y)
    aggregate = 0.
    for xi, yi in zip(x, y):
        aggregate += (xi - mx) * (yi - my)
    return aggregate / (len(x) - 1)


def trace(matrix: list):
    s = 0.
    for i, element in enumerate(matrix):
        s += matrix[i][i]
    return s


def center_data(v):
    mv = mean(v)
    new_v = []
    for i in v:
        new_v.append(i - mv)
    return new_v


def main():
    x = (12, 30, 15, 24, 14, 18, 28, 26, 19, 27)
    y = (20, 60, 27, 50, 21, 30, 61, 54, 32, 57)

    #print('Sample Cov:', sample_cov(x, y))

    something1 = np.array([[1, 2, 3],
                           [4, 15, 6],
                           [7, 8, 9]], np.int8)

    something2 = np.array([[10, 11, 12],
                           [13, 14, 15],
                           [16, 117, 18]], np.int8)

    print(something1.mean())
    print(something2.mean())
    print()


if __name__ == '__main__':
    main()
