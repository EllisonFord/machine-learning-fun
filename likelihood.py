#!/usr/bin/env python3
from math import exp, pi
import matplotlib.pyplot as plt
import numpy as np


class Set:
    def __init__(self, colour, means, std_devs):
        self.colour = colour
        self.means = means
        self.std_devs = std_devs


def gauss_mean(x, mean, std_dev):
    var = std_dev**2
    sub_nom = (x - mean)**2
    sub_den = 2*var
    sub = -sub_nom/sub_den
    base = 1/((2*pi*var)**(1/2))
    return base*exp(sub)


def probability_given():
    pass


red = Set("red", means=(-0.07, 4.83), std_devs=(3.02, 0.98))

green = Set("green", means=(5.19, -5.21), std_devs=(1.14, 1.98))

blue = Set("blue", means=(-3.88, -3.04), std_devs=(1.08, 0.9))



points = []
for i in np.arange(0, 11, 0.1):
    points.append(gauss_mean(i, 5, 1))

plt.plot(points)
plt.show()
