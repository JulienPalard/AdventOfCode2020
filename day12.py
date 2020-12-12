from pathlib import Path
from dataclasses import dataclass

instructions = [
    (lambda line: (line[0], int(line[1:])))(line)
    for line in Path("day12.txt").read_text().split()
    if line
]


@dataclass
class Ship:
    north: int = 0
    east: int = 0
    orientation: int = 0  # 0 for east, in degree

    @property
    def direction(self):
        while self.orientation < 0:
            self.orientation += 360
        return "ESWN"[(self.orientation % 360) // 90]

    @property
    def manhattan_distance(self):
        return abs(self.north) + abs(self.east)


ship = Ship()

facing = "east"
for action, value in instructions:
    if action == "F":
        action = ship.direction
    if action == "N":
        ship.north += value
    if action == "S":
        ship.north -= value
    if action == "E":
        ship.east += value
    if action == "W":
        ship.east -= value
    if action == "L":
        ship.orientation -= value
    if action == "R":
        ship.orientation += value

print("Part 1:", ship, ship.manhattan_distance)


@dataclass
class Waypoint:
    north: int = 1
    east: int = 10
    _orientation: int = 0  # 0 for east, in degree

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        while value < 0:
            value += 360
        value %= 360
        self.north, self.east = [
            (self.north, self.east),
            (-self.east, self.north),
            (-self.north, -self.east),
            (self.east, -self.north),
        ][value // 90]


waypoint = Waypoint()
ship = Ship()

facing = "east"
for action, value in instructions:
    if action == "F":
        ship.north += value * waypoint.north
        ship.east += value * waypoint.east
    if action == "N":
        waypoint.north += value
    if action == "S":
        waypoint.north -= value
    if action == "E":
        waypoint.east += value
    if action == "W":
        waypoint.east -= value
    if action == "L":
        waypoint.orientation -= value
    if action == "R":
        waypoint.orientation += value

print("Part 2:", ship, ship.manhattan_distance)
