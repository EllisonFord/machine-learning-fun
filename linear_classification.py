#!/usr/bin/env python3
import matplotlib.pyplot as plt
from math import exp


def softmax(predictions):
    denominator = 0.0
    for prediction in predictions:
        denominator += exp(prediction)
    return [exp(x) / denominator for x in predictions]


def hyperplane(w, w0, N=range(100)):
    samples = []
    for x in N:
        samples.append(w*x+w0)
    return samples


def main(*args, **kwargs):

    predictions = [1, 2, 2, 4, 1]

    sm_predictions = softmax(predictions)

    print(sm_predictions)

    sample_range = range(5)

    plot1 = hyperplane(1, 1, sample_range)
    plot2 = hyperplane(2, 2, sample_range)
    plot3 = hyperplane(3, 3, sample_range)
    plot4 = hyperplane(0, 0, sample_range)
    plot5 = hyperplane(-1, -1, sample_range)
    plot6 = hyperplane(-2, -2, sample_range)
    plot7 = hyperplane(-3, -3, sample_range)

    plt.plot(sample_range, plot1)
    plt.plot(sample_range, plot2)
    plt.plot(sample_range, plot3)
    plt.plot(sample_range, plot4)
    plt.plot(sample_range, plot5)
    plt.plot(sample_range, plot6)
    plt.plot(sample_range, plot7)
    plt.show()



if __name__ == '__main__':
    main()
