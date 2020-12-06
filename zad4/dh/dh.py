from random import getrandbits
from sympy.ntheory import primitive_root, nextprime

BITS = 128

n = nextprime(getrandbits(BITS))
g = primitive_root(n)

assert(1 < g < n)

# A computes X
x = getrandbits(BITS)
X = pow(g, x, n)

# B computes Y
y = getrandbits(BITS)
Y = pow(g, y, n)

# A computes k
ka = pow(Y, x, n)

# B computes k
kb = pow(X, y, n)

assert (ka == kb)

print(hex(ka))
