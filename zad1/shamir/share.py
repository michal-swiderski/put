#!/usr/bin/env python3
from random import randint
from sys import argv

import numpy as np

PRIME = 1523


def mod(a, n):
    return a % n if a > 0 else a % n - n


def pretty_polynomial(coeffs):
    pretty = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        pretty.append(str(coeff) + (f'x^{degree - i}' if degree - i > 0 else ''))
    return ' + '.join(pretty)


num_shares = int(argv[1])
t = int(argv[2])
secret = int(argv[3])

coeffs = [randint(0, PRIME - 1) for _ in range(t - 1)]
coeffs.append(secret)

shares = [(i, mod(np.polyval(coeffs, i), PRIME)) for i in range(1, num_shares + 1)]

print(f'Generated polynomial: f(x) = {pretty_polynomial(coeffs)}')

print(f'Generated shares:')
for x, y in shares:
    print(f'f({x}) = {y} -> ({x}, {y})')
