#!/usr/bin/env python3
from math import sqrt, cos


def l_one_norm(x, x_new):  # Given 2 tuples, find the distance between them
    s = 0.0
    features = len(x)
    for feature in range(features):
        s += abs(x[feature] - x_new[feature])
    return s


def l_two_norm(x, x_new):  # Euclidean distance
    s = 0.0
    features = len(x)
    for feature in range(features):
        s += (x[feature] - x_new[feature])**2
    return sqrt(s)


def l_inf_norm(x, x_new):
    features = len(x)
    max_val = 0.0
    for feature in range(features):
        current_val = abs(x[feature] - x_new[feature])
        if current_val > max_val:
            max_val = current_val
    return max_val


def mahalanobis():
    pass


def k_nn_weighted(X, Y, new_x, distance_measure='euclidean'):
    pass


def one_nn(X, Y, new_x, distance_measure='euclidean'):
    pass


def k_nn(X, Y, new_x, distance_measure='euclidean'):
    pass


def main():

    X = ((1, 2),
         (1, 5))

    x_new = (2, 3)

    Y = (1,
         1,
         1,
         1,
         0,
         0)

    print(l_one_norm(X[1], x_new))

    print(l_two_norm(X[1], x_new))

    print(l_inf_norm(X[1], x_new))




if __name__ == '__main__':
    main()
