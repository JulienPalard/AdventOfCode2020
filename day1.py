from pathlib import Path
from itertools import combinations

lines = Path("day1.txt").read_text().split("\n")
values = [int(line) for line in lines if line]
for l, r in combinations(values, r=2):
    if l + r == 2020:
        print(l * r)

for a, b, c in combinations(values, r=3):
    if a + b  + c == 2020:
        print(a * b * c)
