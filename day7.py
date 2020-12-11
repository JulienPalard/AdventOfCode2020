from pathlib import Path
import re
from itertools import chain

rules = Path("day7.txt").read_text().strip()


def parse_rule(rule):
    rule = rule.rstrip(".")
    left, right = rule.split(" contain ")
    can_contain = []
    for contain in right.split(", "):
        if contain == "no other bags":
            continue
        else:
            qty, color = re.match("([0-9]) (.*) bags?", contain).groups()
            can_contain.append((int(qty), color))
    return [left.removesuffix(" bags"), can_contain]


RULES = dict(parse_rule(line) for line in rules.split("\n"))


def resolve_rules(color):
    return RULES[color] + list(
        chain(*[resolved for qty, c in RULES[color] if (resolved := resolve_rules(c))])
    )


RESOLVED_RULES = {color: resolve_rules(color) for color in RULES.keys()}


def can_contain(contained_color):
    for container_color, can_contain in RESOLVED_RULES.items():
        if contained_color in {color for qty, color in can_contain}:
            yield container_color


def count_bags(color):
    if not RULES[color]:
        return 1
    return 1 + sum(qty * count_bags(color) for qty, color in RULES[color])


print("Part 1:", len(set(can_contain("shiny gold"))))
print("Part 2:", count_bags("shiny gold") - 1)
