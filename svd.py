#!/usr/bin/env python3

import numpy as np


U, SIG, V = range(3)

A = np.array([[7, 2.5],
              [2, 0]])


SVD = np.linalg.svd(A)

print('\nU')
print(SVD[U])

print('\nSIGMA')
print(SVD[SIG])

print('\nV')
print(SVD[V])

print('\nPutting things back?')
R = SVD[U] @ SVD[SIG] @ SVD[V].T
print(R)

print('\nProjected:')
P = SVD[U] @ SVD[SIG]
print(P)


summand = 0.
for row in SVD[U]:
    summand += row[0]**2
print(np.sqrt(summand))
