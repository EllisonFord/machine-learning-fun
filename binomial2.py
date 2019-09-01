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
    print('Binomial:', binomial(total, choose), 'Single:', (p**choose) * (1-p)**(total-choose))
    return binomial(total, choose)*(p**choose) * (1-p)**(total-choose)


def main():
    n = 10
    p = 0.5
    maximum = n+1
    minimum = 0

    # print(pr(p=p, total=n, selection=18))
    print()
    results = []
    for k in range(minimum, maximum):
        results.append(pr(p=p, total=n, choose=k))
    print()

    print('Integral of results:', sum(results))

    # Plot
    plt.bar(range(minimum, maximum), results)
    plt.xlabel('k')
    plt.ylabel('Probability of Heads given this Coin')
    plt.title(f'{n} coin flips')
    plt.show()

    print(f'We have a high probability of getting {results.index(max(results))} heads in this experiment.')

    print('Mean:', mean(n, p))

    print('Variance:', variance(n, p))


if __name__ == '__main__':
    main()
