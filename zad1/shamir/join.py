#!/usr/bin/env python3
from fractions import Fraction
from math import fmod
from sys import argv

import numpy as np

PRIME = 1523


def find_inverted_elem(element, n):
    for i in range(2, n):
        if (i * element) % n == 1:
            return i


def mod(a, n):
    frac = Fraction.from_float(a).limit_denominator(10000)
    if frac.denominator == 1:
        return fmod(a, n)
    else:
        return (frac.numerator * find_inverted_elem(frac.denominator, n)) % n


def pretty_polynomial(coeffs):
    pretty = ''
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        if coeff > 0 and i > 0:
            pretty += ' + '
        if coeff < 0:
            pretty += ' - '
        pretty += str(round(abs(coeff), 2)) + (f'x^{degree - i}' if degree - i > 0 else '')
    return pretty


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
