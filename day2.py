import re
from pathlib import Path
from itertools import combinations

lines = Path("day2.txt").read_text().split("\n")
values = [re.match(r"(\d+)-(\d+) (.): (.*)", line).groups() for line in lines if line]

# Part 1
ok_passwords = 0
for minimum, maximum, letter, password in values:
    if int(minimum) <= password.count(letter) <= int(maximum):
        ok_passwords += 1
print(ok_passwords)

# Part 2
ok_passwords = 0
for pos1, pos2, letter, password in values:
    letter1 = password[int(pos1) - 1]
    letter2 = password[int(pos2) - 1]
    if (letter1 == letter) ^ (letter2 == letter):
        ok_passwords += 1
print(ok_passwords)
