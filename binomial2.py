#!/usr/bin/env python3
from math import factorial as fac
import matplotlib.pyplot as plt
from math import sqrt


def mean(n, p):
    return n*p


def variance(n, p):
    return n*p*(1-p)


def std_dev(var):
    return sqrt(var)


def binomial(total, choose):
    try:
        binom = fac(total) // fac(choose) // fac(total - choose)
    except ValueError:
        binom = 0
    return binom


def pr(p, total, choose):
    return binomial(total, choose)*(p**choose) * (1-p)**(total-choose)


n = 20
p = 0.82
maximum = 21
minimum = 18

#print(pr(p=p, total=n, selection=18))

results = []
for k in range(minimum, maximum):
    results.append(pr(p=p, total=n, choose=k))

print(sum(results))

plt.bar(range(minimum, maximum), results)

plt.show()

print(mean(n, p))

print(variance(n, p))
