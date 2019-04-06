#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def trace(matrix):
    s = 0.0
    for i, element in enumerate(matrix):
        s += matrix[i][i]
    return s


def main(*args, **kwargs):

    something = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

    print(trace(something))



if __name__ == '__main__':
    main()
