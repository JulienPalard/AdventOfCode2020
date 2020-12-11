from itertools import combinations, count
from pathlib import Path

def is_valid(number, previous_ones):
    return number in {a + b for a, b in combinations(previous_ones, 2)}

def check(numbers, prev, preamble):
    for i in range(preamble, len(numbers)):
        n, prev_n= numbers[i], numbers[i-prev:i]
        if not is_valid(n, prev_n):
            return n

input = [int(i) for i in Path("day9.txt").read_text().split("\n") if i]

print("Part 1:", invalid_one := check(input, 25, 25))

for wsize in count(2):
    for i in range(len(input) - wsize):
        contiguous = input[i:i+wsize]
        if sum(contiguous) == invalid_one:
            print("Part 2:", min(contiguous) + max(contiguous))
            exit(0)
