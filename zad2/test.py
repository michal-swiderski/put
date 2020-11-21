#!/usr/bin/env python3

from bbs import bbs
from itertools import groupby
from collections import Counter

TEST_SAMPLE = 20000

bbs_result = bbs(TEST_SAMPLE)
if TEST_SAMPLE < 100:
    print(f"Binary representation: {bin(bbs_result)}")
print(f"Random key: {bbs_result}\n")

sequence = [(bbs_result >> i) & 1 for i in range(TEST_SAMPLE)]

# TEST POJEDYNCZYCH BITÓW

count = sum(sequence)
print(f"Liczba jedynek: {count}")
if 9725 < count < 10275:
    print("Test pojedynczych bitów: ok\n")
else:
    print("Test pojedynczych bitów: niepowodzenie\n")

# TEST SERII

for i in [0, 1]:
    series_lengths = Counter([len(list(g)) for k, g in groupby(sequence) if k == i])
    print(sorted(series_lengths.items(), key=lambda el: el[0]))
    failed = False
    six_and_more = sum([0 if i < 6 else series_lengths[i] for i in series_lengths.keys()])
    if 2315 < series_lengths.get(1, 0) < 2685 \
            and 1114 < series_lengths.get(2, 0) < 1386 \
            and 527 < series_lengths.get(3, 0) < 723 \
            and 240 < series_lengths.get(4, 0) < 384 \
            and 103 < series_lengths.get(5, 0) < 209 \
            and 103 < six_and_more < 209:
        pass
    else:
        failed = True
        break

if not failed:
    print("Test serii: ok\n")
else:
    print("Test serii: niepowodzenie\n")

# TEST DŁUGIEJ SERII
max_serie = max(series_lengths.keys())
print(f"Maksymalna długość serii: {max_serie}")
if max_serie < 26:
    print("Test długiej serii: ok\n")
else:
    print("Test długiej serii: niepowodzenie\n")

# TEST POKEROWY

parts = [tuple(sequence[i:i + 4]) for i in range(0, TEST_SAMPLE, 4)]
counter = Counter(parts).values()

x = (16 / 5000) * sum((x * x for x in counter)) - 5000

print(f"x = {x}")
if 2.16 < x < 46.17:
    print("Test pokerowy: ok\n")
else:
    print("Test pokerowy: niepowodzenie\n")
