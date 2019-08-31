#!/usr/bin/env python3
from math import factorial as fac
import matplotlib.pyplot as plt


def binomial(total, selection):
    try:
        binom = fac(total) // fac(selection) // fac(total - selection)
    except ValueError:
        binom = 0
    return binom


def p(pr, total, selection):
    return binomial(total, selection)*(pr**selection) * (1-pr)**(total-selection)


maximum = 25
minimum = 5

print(p(pr=0.82, total=20, selection=18))

results = []
for i in range(minimum, maximum):
    results.append(p(pr=0.82, total=20, selection=i))
print(sum(results))

plt.bar(range(minimum, maximum), results)

plt.show()
