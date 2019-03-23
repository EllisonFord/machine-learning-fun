#!/usr/bin/env python3

from math import factorial


def binomial(n, x):
    if x > n:
        print('x is higher than n. Please correct.')
        return
    return factorial(n)/(factorial(n-x)*factorial(x))


def pr(events, single_event_pr):
    pass


def main():
    print(binomial(5, 3))


if __name__ == '__main__':
    main()
