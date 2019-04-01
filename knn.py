#!/usr/bin/env python3
from heapq import nsmallest
from math import sqrt

POSITION, LABEL = range(2)


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


def get_distances(X, Y, new_x, distance_measure='l2'):
    xy_set = zip(X, Y)
    all_distances = []
    for item in xy_set:
        if distance_measure is 'l1':
            all_distances.append((l_one_norm(item[POSITION], new_x), item[LABEL]))
        if distance_measure is 'l2':
            all_distances.append((l_two_norm(item[POSITION], new_x), item[LABEL]))
        if distance_measure is 'l_inf':
            all_distances.append((l_inf_norm(item[POSITION], new_x), item[LABEL]))
    return all_distances


def k_nn_weighted(X, Y, new_x, distance_measure='euclidean'):
    distances = get_distances(X, Y, new_x, distance_measure)
    pass


def one_nn(X, Y, new_x, distance_measure='l2'):
    distances = get_distances(X, Y, new_x, distance_measure)
    return min(distances)[LABEL]


def k_nn(k, X, Y, new_x, distance_measure='l2'):
    distances = get_distances(X, Y, new_x, distance_measure)

    normalisation_dist = sum(distances[POSITION])

    print('distances_position:', distances[POSITION])

    print('Base dist:', normalisation_dist)

    something = nsmallest(k, distances[POSITION])

    for distance in distances:
        print(distance)

    print(f'Smallest {k} distances:', something)


def main():

    X = ((1, 2),
         (1, 5))

    Y = (1,
         0)

    x_new = (1, 5)

    print('New point will be:', one_nn(X, Y, x_new))

    print('L1 Norm:', l_one_norm(X[1], x_new))

    print('L2 Norm:', l_two_norm(X[1], x_new))

    print('L_Inf Norm:', l_inf_norm(X[1], x_new))

    print('1-NN classification:', one_nn(X, Y, x_new))

    print('k-NN classification:', k_nn(2, X, Y, x_new))

    print('')


if __name__ == '__main__':
    main()
