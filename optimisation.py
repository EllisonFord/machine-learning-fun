#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def gravitational_force(mass_1, mass_2, d):
    g = 6.67408e-11
    return (g*mass_1*mass_2)/(d**2)


def gravity(mass, d):
    g = 6.67408e-11
    return (g*mass)/(d**2)


def momentum(grads: list, lr, gamma=0.5):
    m_t = 0.
    weight = 0.

    for grad in grads:
        m_t = lr*grad+gamma*m_t
        print('m_t:', m_t)
        weight = weight - m_t
        print('weight:', weight)


def main(*args, **kwargs):

    earth_mass = 5.972e24
    earth_radius = 6.371e6
    r = gravity(earth_mass, earth_radius)
    print(round(r, 4), 'm/s')

    r = gravitational_force(earth_mass, 80, earth_radius)
    print(round(r, 4), 'N')

    # momentum([5, 7, 3, 1], lr=1)


if __name__ == '__main__':
    main()
