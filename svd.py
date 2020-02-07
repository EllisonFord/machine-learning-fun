#!/usr/bin/env python3

import numpy as np


A = np.array([[7, 2.5],
              [2, 0]])


U, SIG, V = np.linalg.svd(A)

print(U)

print('\nU')
print(U)

print('\nSIGMA')
print(SIG)

print('\nV')
print(V)

print('\nPutting things back?')
R = U @ SIG @ V.T
print(R)

print('\nProjected:')
P = U @ SIG
print(P)


summand = 0.
for row in U:
    summand += row[0]**2
print(np.sqrt(summand))


for row in V:
    summand = sum(row**2)
    break
print(np.sqrt(summand))
