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


def test_set(x, y, P):
    for s in range(P+1):
        res = (1-s/P)*x + (s/P)*y
        print(res)


def test_func(x, y, P):
    for s in range(P+1):
        lam = s/P
        lhs = lam*f(x) + (1-lam)*f(y)
        rhs = f(lam*x + (1-lam)*y)
        check(lhs, rhs)


def plot_it(x, y, P):
    y_pts = []
    for s in range(x, y+1):
        y_pts.append(-1)


P = 50

x = 15

y = -15

test_func(x, y, P)
plot_it(x, y, P)
