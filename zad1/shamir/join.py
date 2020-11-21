from sys import argv
from random import randint
from functools import reduce
from math import floor
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

# num_shares = int(input("Number of shares: "))
# t = int(input("t: "))
# secret = int(input("Secret: "))

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
        l = np.polymul(l, [1/(xi - xj), xj / (xi - xj)])

    print(f'l_{i}(x) = {pretty_polynomial(l)}')
    yi = shares[i][1]
    yl_mod = mod(yi * l[-1], PRIME)
    # print(f'{yi} * {l[-1]} mod {PRIME} = {yl_mod}')
    secret += mod(yi * l[-1], PRIME)


print(f'Reconstructed secret: {secret}')