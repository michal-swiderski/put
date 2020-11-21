#!/usr/bin/env python3

from sys import argv

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def xor(a, b):
    return (int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')).to_bytes(max(len(a), len(b)), 'big')


KEY = get_random_bytes(16)
IV = get_random_bytes(16)

input_file = open(argv[1], 'rb')
output = open(argv[2], 'wb')
block_ciphertext = None
cipher = AES.new(KEY, AES.MODE_ECB)
while block := input_file.read(16):
    if len(block) < 16:
        block = pad(block, 16)
    xored = xor(block, block_ciphertext) if block_ciphertext else xor(block, IV)
    block_ciphertext = cipher.encrypt(xored)
    output.write(block_ciphertext)

input_file.close()
output.close()
print(f'KEY={KEY.hex()}')
print(f'IV={IV.hex()}')
print(f'openssl enc -d -aes-128-cbc -iv {IV.hex()} -K {KEY.hex()} -nosalt -in {argv[2]} -out decrypted')
