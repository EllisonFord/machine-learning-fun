#!/usr/bin/env python3

import numpy as np
from math import log2


def pr(items_in_class, sum_items_all_classes):
    return items_in_class / sum_items_all_classes


def i_error(prob):
    return 1-prob


def diff_i(s, t):
    return i_error(t) - pr(0, 1)*i_error(0.5) - pr(0, 1)*i_error(0.5)


def i_entropy(t):
    i_h = 0
    tot = len(t)
    for i in t:
        if i is 0:
            continue
        i_h -= pr(i, tot)*log2(pr(i, tot))
    return i_h


def i_gini(t):
    s = 0
    tot = len(t)
    for i in t:
        s += pr(i, tot)
    return 1 - s


def main():

    tee = range(10)

    print(i_entropy(tee))

    print(i_gini(tee))


if __name__ == '__main__':
    main()
