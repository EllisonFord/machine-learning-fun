#!/usr/bin/env python3
from functions_script import plt
from random import choice


def mle_coin(large_n, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, large_n + 1):
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


def map_throws(large_n, a, b, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, large_n+1):
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


def full_bayesian_throws(large_n, a, b, fair=True):
    results = []
    heads, tails = 0, 0
    for n in range(1, large_n+1):
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


def play(large_n, a, b, fair=True):
    results_mle = []
    results_map = []
    results_bayes = []
    heads, tails = 0, 0  # Initialise our counters
    for n in range(1, large_n+1):
        outcome = choice([True, False])  # We flip the coin here
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


def report(data, analysis):
    print(f'Last prediction of {analysis} is: {data[-1]}')


def main():

    # Game setting
    fair_coin = True
    large_n = 50  # Number of throws

    # Prior beliefs
    a = 50  # a: prior belief of being tails
    b = 50  # b: prior belief of NOT being tails

    # Play and get the results
    mle, max_a_post, bayes = play(large_n, a, b, fair=fair_coin)

    title = 'Maximum Likelihood Estimation'
    # mle_coin(N, fair=fair_coin)
    plot(mle, title=title)
    report(mle, title)

    title = 'Maximum a Posteriori'
    # results = map_throws(N, a, b, fair=fair_coin)
    plot(max_a_post, prior_belief=a/(a+b), title=title)
    report(max_a_post, title)

    title = 'Full Bayesian'
    # results = full_bayesian_throws(N, a, b, fair=fair_coin)
    plot(bayes, prior_belief=a/(a+b), title=title)
    report(bayes, title)


if __name__ == '__main__':
    main()
