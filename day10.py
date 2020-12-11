from itertools import groupby
from collections import Counter
from math import factorial
from pathlib import Path

def ways_to_remove(n):
    if n < 2:
        return 0
    if n == 2:
        return 2
    return 1 + n - 1 + factorial(n - 1) // factorial(2) // factorial(n-3)


def rle(s):
    for k, g in groupby(s):
        yield k, len(list(g))


input = [int(x) for x in Path("day10.txt").read_text().split() if x]
jumps = [a - b for a, b in zip(sorted(input), [0] + list(sorted(input)))]
counts = Counter(jumps)

print("Part 1:", (counts[3] + 1) * counts[1])

total = 1
for k, size in rle(jumps):
    if k == 1 and size > 1:
        total *= ways_to_remove(size)
print("Part 2:", total)
