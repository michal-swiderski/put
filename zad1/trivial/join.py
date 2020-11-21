from sys import argv
from random import randint
from functools import reduce

k = int(argv[1])
shares = map(int, argv[2:])

print(sum(shares) % k)