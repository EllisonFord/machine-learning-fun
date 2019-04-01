#!/usr/bin/env python3
from math import log10
import numpy as np


def pr(i, s):
    return i / s


def information_gain(i_main_branch, i_left, i_right, pr_left, pr_right):
    return i_main_branch - i_left*pr_left - i_right*pr_right


def i_error(data):  # Information Classification Error
    total = sum(data)
    highest_prob = 0.0
    for i in data:
        if pr(i, total) > highest_prob:
            highest_prob = pr(i, total)
    return 1 - highest_prob


def i_entropy(t):
    total = sum(t)
    i_h = 0.0
    for i in t:
        if i is 0:  # Special case
            continue
        i_h += pr(i, total)*log10(pr(i, total))
    return -i_h


def i_gini(data):
    total = sum(data)
    s = 0.0
    for i in data:
        s += pr(i, total)**2
    return 1 - s


def main():

    data_m = (67, 65, 168)
    total_set = sum(data_m)
    print('Error:', i_error(data_m))
    print('Entropy:', i_entropy(data_m))
    print('Gini index:', i_gini(data_m))
    print()

    data_l = (40, 60)
    print('Error:', i_error(data_l))
    print('Entropy:', i_entropy(data_l))
    print('Gini index:', i_gini(data_l))
    print()

    data_r = (0, 100)
    print('Error:', i_error(data_r))
    print('Entropy:', i_entropy(data_r))
    print('Gini index:', i_gini(data_r))
    print()

    pr_l = sum(data_l)/total_set
    pr_r = sum(data_r)/total_set
    print('IG Error:', information_gain(i_error(data_m), i_error(data_l), i_error(data_r), pr_l, pr_r))
    print('IG Gini:', information_gain(i_gini(data_m), i_gini(data_l), i_gini(data_r), pr_l, pr_r))
    print('IG Entropy:', information_gain(i_entropy(data_m), i_entropy(data_l), i_entropy(data_r), pr_l, pr_r))


if __name__ == '__main__':
    main()
