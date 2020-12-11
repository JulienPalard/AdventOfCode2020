from functools import reduce
from operator import mul
from pathlib import Path

example_map = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().split()

map = Path("day3.txt").read_text().strip().split()


all_encounters = []
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    width = len(map[0])
    height = len(map)
    current_column = 0
    encounters = 0
    for line in range(0, height, down):
        if map[line][current_column % width] == ".":
            pass
        else:
            encounters += 1
        current_column += right
    print(f"{right=} {down=} {encounters=}")
    all_encounters.append(encounters)


print("mul", reduce(mul, all_encounters))
