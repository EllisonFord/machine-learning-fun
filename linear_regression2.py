#!/usr/bin/env python3
import matplotlib.pyplot as plt
from functions_script import vector_mean as mean


def b_1(x, y):
    mx = mean(x)
    my = mean(y)
    numerator = denominator = 0.
    for xi, yi in zip(x, y):
        numerator += (xi - mx) * (yi - my)
        denominator += (xi - mx) ** 2
    return numerator / denominator


def b_0(x, y, b1):
    return (sum(y) - (b1 * sum(x))) / len(x)


def get_b0_b1(x, y):
    b1 = b_1(x, y)
    b0 = b_0(x, y, b1)
    return b0, b1


def main():

    xv = (65, 65, 62, 67, 69, 65, 61, 67)

    yv = (105, 125, 110, 120, 140, 135, 95, 130)

    # plt.scatter(x=xv, y=yv)
    # plt.show()

    b, m = get_b0_b1(xv, yv)

    # plt.plot(xv, yv, '.')
    # plt.plot(m, b, '-')
    # plt.show()

    print(get_b0_b1(xv, yv))


if __name__ == '__main__':
    main()

