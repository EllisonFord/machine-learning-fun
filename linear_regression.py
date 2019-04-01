#!/usr/bin/env python3
import matplotlib.pyplot as plt
from random import gauss
from math import sin, pi


def noisy_sine(samples, precision):
    Z = []  # Targets Z
    for x in range(samples+1):
        Z.append(sin((2*pi*x)/samples) + gauss(0, 1/precision))
    plt.scatter(range(samples+1), Z)
    plt.title('Generated Noisy Sinusoid')
    plt.show()
    return Z


def main():
    Z = noisy_sine(samples=10, precision=10)


if __name__ == '__main__':
    main()
