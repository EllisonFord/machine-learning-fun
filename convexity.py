#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def check(lhs, rhs):
    if lhs >= rhs:
        print('+ Convex')
    else:
        print('- Concave')


def f(x):
    return -x*x*x


def f_2(x):
    return -x*x*x + 2*x*x + 5


def test_set(x, y, p):
    for s in range(p+1):
        res = (1-s/p)*x + (s/p)*y
        print(res)


def test_func(x, y, p):
    for s in range(p+1):
        lam = s/p
        lhs = lam*f(x) + (1-lam)*f(y)
        rhs = f(lam*x + (1-lam)*y)
        check(lhs, rhs)


def plot_it(x, y, p):
    y_pts = []
    for s in range(x, y+1):
        y_pts.append(-1)


def main(*args, **kwargs):

    p = 50

    x = 15

    y = -15

    test_func(x, y, p)
    plot_it(x, y, p)


if __name__ == '__main__':
    main()
