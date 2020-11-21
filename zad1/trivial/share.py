from sys import argv
from random import randint
from functools import reduce

assert(len(argv) == 4)

n = int(argv[1])
k = int(argv[2])
secret = int(argv[3])

assert(secret >= 0 and secret < k)

shares = [randint(0, k - 1) for _ in range(n - 1)]
shares.append(reduce(lambda a, b: a - b, shares, secret))

print('\n'.join(map(str, shares)))
