from pathlib import Path
from string import ascii_lowercase

# Part 1
s = 0
for group in Path("day6.txt").read_text().split("\n\n"):
    group = group.replace("\n", "")
    s += len(set(group))
print(s)

# Part 2
s = 0
for group in Path("day6.txt").read_text().split("\n\n"):
    answered_yes = set(ascii_lowercase)
    for people in group.split("\n"):
        if people:
            answered_yes &= set(people)
    s += len(answered_yes)
print(s)
