#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def momentum(grads: list, lr, gamma=0.5):
    m_t = 0.
    weight = 0.

    for grad in grads:
        m_t = lr*grad+gamma*m_t
        print('m_t:', m_t)
        weight = weight - m_t
        print('weight:', weight)


def adam():
    pass


def main(*args, **kwargs):
    momentum([5, 7, 3, 1], lr=1)


if __name__ == '__main__':
    main()
