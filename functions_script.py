#!/usr/bin/env python3
from math import sin, pi, exp, factorial as fact
import matplotlib.pyplot as plt
import random


def mean(v):
    return sum(v)/len(v)


def sigmoid(x):
    return 1/(1+exp(-x))


def noisy_sine(samples, precision):
    X = []  # Targets Z
    for x_i in range(samples+1):
        X.append(sin((2*pi*x_i)/samples) + random.gauss(0, 1/precision))
    plt.scatter(range(samples+1), X)
    plt.title('Generated Noisy Sinusoid')
    plt.show()
    return X


def gaussian(alpha, x, sigma):
    return alpha*exp(-(x*x/sigma*sigma))


def softmax(predictions):
    denominator = 0.
    for prediction in predictions:
        denominator += exp(prediction)
    return [exp(x) / denominator for x in predictions]


def binomial(total, choose):
    if choose > total:
        print('choose is higher than total. Please correct.')
        return
    try:
        binom = fact(total) // fact(choose) // fact(total - choose)
    except ValueError:
        binom = 0
    return binom
