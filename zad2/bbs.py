#!/usr/bin/env python3

from random import getrandbits, randint
from sympy import nextprime

BITS = 256

def get_prime():
    prime = nextprime(getrandbits(BITS))
    while prime % 4 != 3:
        prime = nextprime(prime)
    return prime


def bbs(n):
    p = get_prime()
    q = get_prime()
    N = p * q

    x = randint(2, N - 1)
    while x == p or x == q:
        x = randint(2, N - 1)

    xi = (x * x) % N
    result = 0
    for i in range(n):
        xi = (xi * xi) % N
        if xi % 2 == 1:
            result |= (1<<i)
    return result


if __name__ == "__main__":
    from sys import argv

    print(bbs(int(argv[1])))