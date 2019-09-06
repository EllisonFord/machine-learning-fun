#!/usr/bin/env python3
from functions_script import binomial
import matplotlib.pyplot as plt
from math import sqrt


def mean(n, p):
    return n*p


def variance(n, p):
    return n*p*(1-p)


def std_dev(var):
    return sqrt(var)


def pr(p, total, choose, verbose=False):
    if verbose:
        print(f'{total} choose {choose} has {binomial(total, choose)} combinations. Single probability: {(p**choose) * (1-p)**(total-choose)}')
    return binomial(total, choose)*(p**choose) * (1-p)**(total-choose)


def main():
    n = 40
    p = 0.12
    maximum = n+1
    minimum = 0

    # print(pr(p=p, total=n, selection=18))
    print()
    results = []
    for k in range(minimum, maximum):
        results.append(pr(p=p, total=n, choose=k, verbose=True))
    print()

    print('Integral of results:', sum(results))

    # Plot
    plt.bar(range(minimum, maximum), results)
    plt.xlabel('Number of Heads')
    plt.ylabel('Likelihood')
    plt.title(f'{n} coin flips')
    plt.show()

    sorted_results = sorted(results, reverse=True)

    print(f'We have the highest probability of getting {results.index(max(results))} heads in this experiment, '
          f'followed by {results.index(sorted_results[1])} heads.')

    print('Mean:', mean(n, p))

    print('Variance:', variance(n, p))


if __name__ == '__main__':
    main()
