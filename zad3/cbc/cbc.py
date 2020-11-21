#!/usr/bin/env python3

from sys import argv

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

KEY = get_random_bytes(16)
IV = get_random_bytes(16)

input_file = open(argv[1], 'rb')
content = pad(input_file.read(), 16)
input_file.close()

parts = [content[i:i + 16] for i in range(0, len(content), 16)]

ciphertext = bytes()
block_ciphertext = None
for part in parts:
    if block_ciphertext is None:
        block = (int.from_bytes(part, 'big') ^ int.from_bytes(IV, 'big')).to_bytes(len(part), 'big')
    else:
        block = (int.from_bytes(part, 'big') ^ int.from_bytes(block_ciphertext, 'big')).to_bytes(len(part), 'big')
    cipher = AES.new(KEY, AES.MODE_ECB)
    block_ciphertext = cipher.encrypt(block)
    ciphertext += block_ciphertext

print(f'KEY={KEY.hex()}')
print(f'IV={IV.hex()}')
print(f'openssl enc -d -aes-128-cbc -in ./encrypted -out decrypted.jpg -iv {IV.hex()} -K {KEY.hex()} -nosalt')
output = open(argv[2], 'wb')
output.write(ciphertext)
output.close()
