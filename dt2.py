#!/usr/bin/env python3
from math import log, exp, e
import tabulate
import numpy as np
from numpy import genfromtxt

my_data = genfromtxt('homework_01_dataset.csv', delimiter=',')


type(my_data)


with open('homework_01_dataset.csv', mode='r') as f:

    line_count = 0

    #print(tabulate.tabulate(csv_reader, headers=['x1', 'x2', 'x3', 'z'], tablefmt="orgtbl"))

    """
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}\t{row[1]}\t{row[2]}')
            line_count += 1
    print(f'\nProcessed {line_count} lines.')

    """
