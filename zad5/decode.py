#!/usr/bin/env python3
# ./decode.py [input image] [output file]
from sys import argv, byteorder

import imageio

from utils import sizeof_fmt, to_coords


def read_byte(img, n):
    first_bit = n * 8

    byte = 0
    for offset in range(8):
        coords = to_coords(img.shape, first_bit + offset)
        byte |= ((1 & img[coords]) << offset)

    return byte


img = imageio.imread(argv[1])
size = int.from_bytes((read_byte(img, i) for i in range(4)), byteorder)

output = open(argv[2], 'wb')

buf = bytes([read_byte(img, i + 4) for i in range(size)])
output.write(buf)

print(f'Read {sizeof_fmt(size)}')

output.close()
