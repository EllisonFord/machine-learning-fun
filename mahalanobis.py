#!/usr/bin/env python3
from functions_script import vector_mean as mean
from math import sqrt


def mahalanobis():
    pass


def main():

    a = ((6.0, 1.5), (6.5, 3.0), (5.0, 2.0), (5.5, 3.5), (4.0, 2.5), (4.5, 4.0))

    b = ((2.5, 4.0), (2.0, 4.0), (1.5, 4.0), (2.5, 4.5), (2.0, 4.5), (1.5, 4.5))

    x = (4.0, 5.0)

    print(mean(x))


if __name__ == '__main__':
    main()
