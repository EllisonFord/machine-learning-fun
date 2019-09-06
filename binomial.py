#!/usr/bin/env python3
from functions_script import binomial


def gamma(x):
    pass  # integral going on


# Bernoulli Distribution
def bern(x, prob, n=1):
    return (prob**x) * (1-prob)**(n-x)


def coin_mle(sequence):
    # Maximum Likelihood Estimation
    heads, tails = 0, 0
    for event in sequence:
        if event is 'H':
            heads += 1
            print('Heads')
        else:
            tails += 1
    return tails / (tails + heads)


def pr(events, single_event_pr):
    pass


def main(*args, **kwargs):

    flips1 = ('H', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'H')

    mle_flips1 = coin_mle(flips1)

    print(mle_flips1)

    flips2 = ('H', 'H')

    mle_flips2 = coin_mle(flips2)

    print(mle_flips2)

    print(binomial(5, 3))

    print(bern(0.5, 0.5))


if __name__ == '__main__':
    main()
