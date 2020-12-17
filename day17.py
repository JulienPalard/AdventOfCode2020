from pathlib import Path

def neighbors(cube, point4d):
    alive = 0
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            for dz in -1, 0, 1:
                for da in -1, 0, 1:
                    if dx or dy or dz or da:
                        if (point4d[0] + dx, point4d[1] + dy, point4d[2] + dz, point4d[3] + da) in cube:
                            alive += 1
    return alive

def cube_bounds(cube):
    """Returns a 4-tuple of 2-tuples:

    ((minx, max), (miny, maxy), (minz, maxz), (mina, maxa))
    """
    return ((min(p[0] for p in cube.keys()), max(p[0] for p in cube.keys())),
            (min(p[1] for p in cube.keys()), max(p[1] for p in cube.keys())),
            (min(p[2] for p in cube.keys()), max(p[2] for p in cube.keys())),
            (min(p[3] for p in cube.keys()), max(p[3] for p in cube.keys())),)

def cube_print(cube):
    (startx, endx), (starty, endy), (startz, endz), (starta, enda) = cube_bounds(cube)
    for z in range(startz, endz+1):
        print(f"{z=}")
        for a in range(starta, enda):
            print(f"{a=}")
            for y in range(starty, endy+1):
                for x in range(startx, endx+1):
                    print('#' if cube.get((x, y, z)) else '.', end="")
                print()
            print()
        print()

def cycle(cube):
    """During a cycle, all cubes simultaneously change their state
    according to the following rules:

    If a cube is active and exactly 2 or 3 of its neighbors are also
    active, the cube remains active. Otherwise, the cube becomes
    inactive.

    If a cube is inactive but exactly 3 of its neighbors are active,
    the cube becomes active. Otherwise, the cube remains inactive.
    """
    new_cube = {}
    (startx, endx), (starty, endy), (startz, endz), (starta, enda) = cube_bounds(cube)
    for x in range(startx-1, endx+2):
        for y in range(starty-1, endy+2):
            for z in range(startz-1, endz+2):
                for a in range(starta-1, enda+2):
                    if cube.get((x, y, z, a)):
                        if 2 <= neighbors(cube, (x, y, z, a)) <= 3:
                            new_cube[x, y, z, a] = True
                    elif neighbors(cube, (x, y, z, a)) == 3:
                        new_cube[x, y, z, a] = True
    return new_cube

def solve():
    cube = {}
    for y, line in enumerate(Path("day17.txt").read_text().split()):
        for x, item in enumerate(line):
            if item == '#':
                cube[x, y, 0, 0] = True
    for stepno in range(6):
        cube = cycle(cube)
        print(stepno+1, len(cube))

# 112 is too low
solve()
