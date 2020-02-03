#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def check(lhs, rhs, at):
    if lhs >= rhs:
        print('+ Convex at {}'.format(at))
    else:
        print('- Concave at {}'.format(at))


def f(x):
    return -x*x*x


def f_2(x):
    return -x*x*x + 2*x*x + 5


def test_set(x, y, p):
    for s in range(p+1):
        res = (1-s/p)*x + (s/p)*y
        print(res)


def test_func(p_1, p_2, n_samples):
    n = len(n_samples)
    for s in n_samples:
        lam = s/n_samples
        lhs = lam*f(p_1) + (1-lam)*f(p_2)
        rhs = f(lam*p_1 + (1-lam)*p_2)
        check(lhs, rhs, s)


def plot_it(x, y, precision):
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
