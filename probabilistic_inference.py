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


def map_throws(N, a, b, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, N+1):
        outcome = choice([True, False])
        if outcome is True:
            heads += 1
        else:
            tails += 1
        if fair:
            result = max_a_posteriori_coin(t=tails, h=heads, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)
        else:
            result = max_a_posteriori_coin(t=n, h=0, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)

    print('Total num tails:', tails)
    print('Total num heads:', heads)

    return results


def full_bayesian_coin(t, h, a, b):
    numerator = t+a
    denominator = t + a + h + b
    return numerator / denominator


def full_bayesian_throws(N, a, b, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, N+1):
        outcome = choice([True, False])
        if outcome is True:
            heads += 1
        else:
            tails += 1
        if fair:
            result = full_bayesian_coin(t=tails, h=heads, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)
        else:
            result = full_bayesian_coin(t=n, h=0, a=a, b=b)  # t=n means casino will throw Tails every
            results.append(result)
    return results


def play(N, a, b, fair=True):
    results_mle = []
    results_map = []
    results_bayes = []
    heads, tails = 0, 0
    for n in range(1, N+1):
        outcome = choice([True, False])
        if outcome is True:
            tails += 1
        else:
            heads += 1
        if fair:
            result_mle = tails / (heads + tails)
            results_mle.append(result_mle)

            result_map = max_a_posteriori_coin(t=tails, h=heads, a=a, b=b)
            results_map.append(result_map)

            result_bayes = full_bayesian_coin(t=tails, h=heads, a=a, b=b)  # t=n means casino will throw Tails every
            results_bayes.append(result_bayes)
        else:
            result_mle = 1
            results_mle.append(result_mle)

            result_map = max_a_posteriori_coin(t=n, h=0, a=a, b=b)
            results_map.append(result_map)

            result_bayes = full_bayesian_coin(t=n, h=0, a=a, b=b)  # t=n means casino will throw Tails every
            results_bayes.append(result_bayes)

    return results_mle, results_map, results_bayes


def plot(results, title, prior_belief=None):
    plt.plot(results)
    plt.title(title)
    plt.xlabel("Num Throws")
    plt.ylabel("Posterior probability that outcome is Tails")
    if prior_belief is not None:
        plt.axhline(prior_belief, color="orange")
    plt.show()


def main():

    # Game setting
    fair_coin = True
    N = 500  # Number of throws

    # Prior beliefs
    a = 50  # a: prior belief of being tails
    b = 50  # b: prior belief of NOT being tails

    # Play Results
    mle, mapost, bayes = play(N, a, b, fair=fair_coin)

    # Maximum Likelihood Estimation
    # mle_coin(N, fair=fair_coin)
    plot(mle, title="MLE")

    # Maximum a Posteriori
    # results = map_throws(N, a, b, fair=fair_coin)
    plot(mapost, prior_belief=a/(a+b), title="MAP")

    # Full Bayesian
    # results = full_bayesian_throws(N, a, b, fair=fair_coin)
    plot(bayes, prior_belief=a/(a+b), title="Full Bayesian")


if __name__ == '__main__':
    main()