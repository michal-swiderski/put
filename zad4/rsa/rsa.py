from secrets import randbits
from sympy import nextprime
from sys import byteorder as BYTEORDER

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


BITS = 1024
e = 65537

p = nextprime(randbits(BITS))
q = nextprime(randbits(BITS))
n = p * q
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

# messasge
TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing'
print(f'RSA Message: {TEXT}')

#encryption
message = int.from_bytes(bytes(TEXT, 'utf8'), BYTEORDER)
enc = pow(message, e, n)
print(f'RSA ciphertext: {hex(enc)}')

#decryption
dec = pow(enc, d, n)
utf8_decoded = dec.to_bytes(dec.bit_length(), BYTEORDER).decode('utf8')
print(f'Decrypted: {utf8_decoded}')