import numpy as np
from pathlib import Path

def parse_map(map):
    # 0 is floor
    # 1 is empty
    # 2 is occupied
    return np.array([[".L#".index(c) for c in line] for line in map.split()])


def adjacent_part_one(map, x, y):
    # one of the eight positions immediately up, down, left, right, or diagonal from the seat.
    adj = [(+1, +1), (+1, +0), (+1, -1), (+0, +1), (+0, -1), (-1, +1), (-1, +0), (-1, -1)]
    for i, j in adj:
        if y + j >= 0 and x + i >= 0 and x + i < map.shape[0] and y + j < map.shape[1]:
            yield map[x + i, y + j]


def adjacent_part_two(map, x, y):
    # the first seat in each of those eight directions
    adj = [
        (+1, +1),
        (+1, +0),
        (+1, -1),
        (+0, +1),
        (+0, -1),
        (-1, +1),
        (-1, +0),
        (-1, -1),
    ]
    for i, j in adj:
        look_at_x = x
        look_at_y = y
        while (
            look_at_x + i >= 0
            and look_at_y + j >= 0
            and look_at_x + i < map.shape[0]
            and look_at_y + j < map.shape[1]
        ):
            look_at_x += i
            look_at_y += j
            if map[look_at_x, look_at_y] in (1, 2):
                yield map[look_at_x, look_at_y]
                break


def apply_rule(map, adjacency, threshold):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    new_map = map.copy()
    change_state = False
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            if map[x, y] == 1:  # Cell is empty, should we occupy it?
                if all(cell in (0, 1) for cell in adjacency(map, x, y)):
                    change_state = True
                    new_map[x, y] = 2
            if map[x, y] == 2:  # Cell is occupied, should we empty it?
                nearby_occupied_seats = sum(cell == 2 for cell in adjacency(map, x, y))
                if nearby_occupied_seats >= threshold:
                    change_state = True
                    new_map[x, y] = 1
    return new_map, change_state


def show_map(map):
    for line in map:
        print("".join([".L#"[cell] for cell in line]))


input = Path("day11.txt").read_text().strip()

part1 = {"adjacency": adjacent_part_one, "threshold": 4}
part2 = {"adjacency": adjacent_part_two, "threshold": 5}
for part in part1, part2:
    map = parse_map(input)
    while True:
        map, changed = apply_rule(map, **part)
        if not changed:
            show_map(map)
            print(len(map[map == 2]))
            break
