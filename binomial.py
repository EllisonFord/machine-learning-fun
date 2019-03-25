#!/usr/bin/env python3

from math import factorial, exp


def gamma(x):
    pass  # integral going on


def bern(x, prob, n=1):
    # Bernoulli Distribution
    return (prob**x) * (1-prob)**(n-x)


def combinations(n, x):
    if x > n:
        print('x is higher than n. Please correct.')
        return
    return factorial(n)/(factorial(n-x)*factorial(x))


def binomial(x, n, prob):
    return combinations(n, x) * bern(x, prob, n)


def coin_mle(sequence):
    # Maximum Likelihood Estimation
    heads = 0
    tails = 0
    for event in sequence:
        if event is 'H':
            heads += 1
            print('Heads')
        else:
            tails += 1
    return tails / (tails + heads)


def pr(events, single_event_pr):
    pass


def main():

    flips1 = ('H', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'H')

    mle_flips1 = coin_mle(flips1)

    print(mle_flips1)

    flips2 = ('H', 'H')

    mle_flips2 = coin_mle(flips2)

    print(mle_flips2)

    # print(binomial(5, 3))

    print(bern(0.5, 0.5))


if __name__ == '__main__':
    main()
