#!/usr/bin/env python3
import time
from os import stat

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from colorama import Fore, Style

KEY = get_random_bytes(32)
IV = get_random_bytes(16)
NONCE = get_random_bytes(8)

FILES = ['small', 'medium', 'big']
MODES = [AES.MODE_CBC, AES.MODE_ECB, AES.MODE_OFB, AES.MODE_CFB, AES.MODE_CTR]
MODE_NAMES = ['CBC', 'ECB', 'OFB', 'CFB', 'CTR']

PADDING = 9


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Y', suffix)


def measure(fun):
    start = time.time()
    result = fun()
    end = time.time()
    return result, end - start


def table(data):
    print(' ' * PADDING, end='')
    for name in [name.ljust(PADDING) for name in MODE_NAMES]:
        print(name, end='')
    print('')

    for file, row in zip(FILES, data):
        print(sizeof_fmt(stat(file).st_size).ljust(PADDING), end='')

        max_time, min_time = max(row), min(row)
        for t in row:
            color = Fore.RED if t == max_time else (Fore.GREEN if t == min_time else Fore.WHITE)
            print(f'{color}{str(round(t, 5)).ljust(PADDING)}{Style.RESET_ALL}', end='')
        print('')


def get_cipher(mode):
    if mode == AES.MODE_ECB:
        return AES.new(KEY, mode)
    if mode == AES.MODE_CTR:
        return AES.new(KEY, mode, nonce=NONCE)
    return AES.new(KEY, mode, IV)


encrypting_times, decrypting_times = [], []

for i, file_name in enumerate(FILES):
    file = open(file_name, 'rb')
    content = pad(file.read(), 16)
    file.close()

    encrypting_times.append([])
    decrypting_times.append([])

    for mode in MODES:
        ciphertext, t = measure(lambda: get_cipher(mode).encrypt(content))
        encrypting_times[i].append(t)

        plaintext, t = measure(lambda: get_cipher(mode).decrypt(ciphertext))
        decrypting_times[i].append(t)
        assert (content == plaintext)

print('ENCRYPTION [s]')
table(encrypting_times)
print('')
print('DECRYPTION [s]')
table(decrypting_times)
