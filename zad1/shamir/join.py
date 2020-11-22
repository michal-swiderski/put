#!/usr/bin/env python3
from fractions import Fraction
from math import fmod
from sys import argv

import numpy as np

PRIME = 1523


def mod(a, n):
    frac = Fraction.from_float(a).limit_denominator(10000)
    if frac.denominator == 1:
        return fmod(a, n)
    else:
        return (pow(frac.denominator, n - 2, n) * frac.numerator) % n


def pretty_polynomial(coeffs):
    pretty = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        pretty.append(str(coeff) + (f'x^{degree - i}' if degree - i > 0 else ''))
    return ' + '.join(pretty)


raw = list(map(int, argv[1:]))
shares = list(zip(raw[0::2], raw[1::2]))

secret = 0
for i in range(len(shares)):
    l = [1]
    for j in range(len(shares)):
        if j == i:
            continue
        xi = shares[i][0]
        xj = shares[j][0]
        l = np.polymul(l, [1 / (xi - xj), -xj / (xi - xj)])

    print(f'l_{i}(x) = {pretty_polynomial(l)}')
    secret += mod(shares[i][1] * l[-1], PRIME)

print(f'Reconstructed secret: {secret}')
