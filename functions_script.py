#!/usr/bin/env python3


def vector_mean(v: list) -> float:
    return sum(v)/len(v)


def matrix_mean(v: list) -> float:
    return 0.


def sigmoid(x: float) -> float:
    from math import exp
    return 1/(1+exp(-x))


def noisy_sine(samples, precision) -> list:
    import matplotlib.pyplot as plt
    from math import sin, pi
    import random
    xv = []  # X vector
    for x_i in range(samples+1):
        xv.append(sin((2*pi*x_i)/samples) + random.gauss(0, 1/precision))
    plt.scatter(range(samples+1), xv)
    plt.title('Generated Noisy Sinusoid')
    plt.show()
    return xv


def gaussian(alpha, x, sigma) -> float:
    from math import exp
    return alpha*exp(-(x*x/sigma*sigma))


def softmax(predictions: list) -> list:
    from math import exp
    denominator = 0.
    for prediction in predictions:
        denominator += exp(prediction)
    return [exp(x) / denominator for x in predictions]


def binomial(total: int, choose: int) -> int:
    from math import factorial as fact
    if choose > total:
        print('choose is higher than total. Please correct.')
    else:
        try:
            binom = fact(total) // fact(choose) // fact(total - choose)
        except ValueError:
            binom = 0
        return binom
