#!/usr/bin/env python3

import numpy as np
from math import log10


def pr(items_in_class, sum_items_all_classes):
    return items_in_class / sum_items_all_classes


def i_error(data):
    total = sum(data)
    highest_prob = 0.0
    for i in data:
        if pr(i, total) > highest_prob:
            highest_prob = pr(i, total)
    return 1 - highest_prob


def diff_i(s, t):
    return i_error(t) - pr(0, 1)*i_error(0.5) - pr(0, 1)*i_error(0.5)


def i_entropy(t):
    i_h = 0
    total = sum(t)
    for i in t:
        if i is 0:
            continue
        i_h += pr(i, total)*log10(pr(i, total))
    return -i_h


def i_gini(data):
    s = 0
    total = sum(data)
    for i in data:
        s += pr(i, total)**2
    return 1 - s


def main():

    data = range(10)

    data = (10, 30)

    print('Error:', i_error(data))

    print('Entropy:', i_entropy(data))

    print('Gini index:', i_gini(data))



if __name__ == '__main__':
    main()
