#!/usr/bin/env python3
import matplotlib.pyplot as plt
from random import choice


def mle_coin(N, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, N + 1):
        outcome = choice([True, False])
        if outcome is True:
            heads += 1
        else:
            tails += 1
        if fair:
            result = tails / (heads + tails)
            results.append(result)
        else:
            results.append(1)
    return results


def max_a_posteriori_coin(t, h, a, b):
    numerator = t + a - 1
    denominator = h + t + a + b - 2
    return numerator / denominator


def map_throws(N, a, b, fair=True, exercise=False):
    results = []
    heads, tails = 0, 0
    for n in range(1, N+1):
        outcome = choice([True, False])
        if outcome is True:
            heads += 1
        else:
            tails += 1
        if fair:
            result = max_a_posteriori_coin(t=heads, h=tails, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)
        else:
            result = max_a_posteriori_coin(t=n, h=0, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)

    print('Total num tails:', tails)
    print('Total num heads:', heads)

    return results


def plot_it(results, title, prior_belief=0.5):
    plt.plot(results)
    plt.title(title)
    plt.xlabel("Num Throws")
    plt.ylabel("Posterior probability that outcome is Tails")
    plt.axhline(prior_belief, color="orange")
    plt.show()


def full_bayesian_coin():
    pass


def main():

    a = 5  # a, prior belief of being tails
    b = 5  # b, prior belief of NOT being tails
    N = 100  # Number of throws

    # Maximum Lilelihood Estimate
    results = mle_coin(N, fair=False)
    plot_it(results, prior_belief=0.5, title="MLE")

    # Maximum a Posteriori
    results = map_throws(N, a, b, fair=False)
    plot_it(results, prior_belief=0.5, title="MAP")


    # Full Bayesian


if __name__ == '__main__':
    main()
