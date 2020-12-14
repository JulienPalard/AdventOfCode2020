from copy import deepcopy
import re
from pathlib import Path

input = Path("day14.txt").read_text().strip().split("\n")


def parse_mask(mask):
    """Parse a mask.

    Returns a tuple to OR and AND.
    """
    return int(mask.replace("X", "0"), 2), int(mask.replace("X", "1"), 2)


mem = {}
for line in input:
    match = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
    if not match:
        o, a = parse_mask(line.split()[-1])
        continue
    addr = match.group(1)
    data = match.group(2)
    mem[addr] = (int(data) | o) & a

print("Part1:", sum(mem.values()))


def genmask(mask, addr):
    """Apply a v2 mask on an addr."""
    addrs = [[]]
    for maskbit, addrbit in zip(mask, f"{int(addr):036b}"):
        if maskbit == "0":
            for a in addrs:
                a.append(addrbit)
        elif maskbit == "1":
            for a in addrs:
                a.append(1)
        else:
            new = deepcopy(addrs)
            for a in addrs:
                a.append(0)
            for a in new:
                a.append(1)
            addrs += new

    def to_addr(addr):
        return int("".join([str(bit) for bit in addr]), 2)

    return [to_addr(addr) for addr in addrs]


mem = {}
for line in input:
    match = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
    if not match:
        mask = line.split()[-1]
        continue
    data = match.group(2)
    for addr in genmask(mask, match.group(1)):
        mem[addr] = int(data)

print("Part2:", sum(mem.values()))
