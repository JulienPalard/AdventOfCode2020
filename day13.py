from pathlib import Path
from itertools import count
from functools import reduce
from operator import mul

my_depart, ids = Path("day13.txt").read_text().strip().split("\n")
my_depart = int(my_depart)
part1_ids = [int(id) for id in ids.split(",") if id != "x"]
part2_ids = [int(id) if id != "x" else 0 for id in ids.split(",")]
print(my_depart, "\t".join(str(i) for i in part1_ids))


def find_next_bus(ids, my_depart):
    for time in count(my_depart):
        print(time, "\t".join("D" if time % bus_id == 0 else "-" for bus_id in ids))
        for bus_id in ids:
            if time % bus_id == 0:
                return time, bus_id


time, bus_id = find_next_bus(part1_ids, my_depart)
print("Part 1:", (time - my_depart) * bus_id)


def find_next(shift, bus_id, start=0, step=1):
    for time in count(start, step):
        if (time + shift) % bus_id == 0:
            return time


def find_depart(ids):
    start = ids[0]
    step = ids[0]
    for i in range(0, len(ids)):
        if ids[i] == 0:
            continue
        start = find_next(i, ids[i], start, step)
        step = reduce(mul, [i for i in ids[0 : i + 1] if i], 1)
    return start


assert find_depart([17, 0, 13, 19]) == 3417
assert find_depart([67, 7, 59, 61]) == 754018
assert find_depart([67, 0, 7, 59, 61]) == 779210
assert find_depart([67, 7, 0, 59, 61]) == 1261476
assert find_depart([1789, 37, 47, 1889]) == 1202161486

print("Part 2:", find_depart(part2_ids))
