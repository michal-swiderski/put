#!/usr/bin/env python3
# ./encode.py [input image] [file to encode] [output image]
import os
from math import floor
from sys import argv, byteorder

import imageio

from utils import sizeof_fmt, to_coords


def write_byte(img, n, byte):
    first_bit = n * 8

    for offset in range(8):
        coords = to_coords(img.shape, first_bit + offset)
        if 1 & (byte >> offset):
            img[coords] = img[coords] | 1
        else:
            img[coords] = img[coords] & ~1


img = imageio.imread(argv[1])
input_file = open(argv[2], 'rb')

height, width, channels = img.shape
capacity = floor(height * width * channels / 8)

size = os.stat(argv[2]).st_size

if size > capacity:
    print(f'File of size: {sizeof_fmt(size)} is too big')
    exit(1)

size_buf = int.to_bytes(size, 4, byteorder)
write_byte(img, 0, size_buf[0])
write_byte(img, 1, size_buf[1])
write_byte(img, 2, size_buf[2])
write_byte(img, 3, size_buf[3])

while buf := input_file.read(1):
    write_byte(img, input_file.tell() + 3, buf[0])

input_file.close()

imageio.imwrite(argv[3], img)

print(f'Written {sizeof_fmt(size)} out of {sizeof_fmt(capacity)}')
