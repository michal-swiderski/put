#!/usr/bin/env python3

from random import randint
from sys import stdout, argv

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

KEY = get_random_bytes(32)
IV = get_random_bytes(16)
NONCE = get_random_bytes(8)

MODES = [AES.MODE_CBC, AES.MODE_ECB, AES.MODE_OFB, AES.MODE_CTR]
MODE_NAMES = ['CBC', 'ECB', 'OFB', 'CTR']


def get_cipher(mode):
    if mode == AES.MODE_ECB:
        return AES.new(KEY, mode)
    if mode == AES.MODE_CTR:
        return AES.new(KEY, mode, nonce=NONCE)
    return AES.new(KEY, mode, IV)


input_file = open(argv[1], 'rb')
content = input_file.read()
mode = MODES[MODE_NAMES.index(argv[2])]
input_file.close()

ciphertext = get_cipher(mode).encrypt(pad(content, 16))
shift = randint(0, len(ciphertext) * 8)
mangled = (int.from_bytes(ciphertext, 'big') ^ (1 << shift)).to_bytes(len(ciphertext), 'big')

plaintext = get_cipher(mode).decrypt(mangled)

stdout.buffer.write(plaintext)
stdout.flush()
