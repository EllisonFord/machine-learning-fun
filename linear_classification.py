#!/usr/bin/env python3
from math import exp


def softmax(predictions):
    denominator = 0.0
    for prediction in predictions:
        denominator += exp(prediction)
    return [exp(x) / denominator for x in predictions]


def main():

    predictions = [1, 2, 2, 4, 1]

    sm_predictions = softmax(predictions)

    print(sm_predictions)


if __name__ == '__main__':
    main()
