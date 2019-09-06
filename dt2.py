#!/usr/bin/env python3

from math import log, exp, e
import numpy as np
import pandas


def main():

    r = pandas.read_csv('homework_01_dataset.csv', header=0)

    # print(r['z'])

    print(r)


if __name__ == '__main__':
    main()
