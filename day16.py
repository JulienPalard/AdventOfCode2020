from functools import reduce
from operator import mul
import re
from pathlib import Path

rules, my_ticket, nearby_tickets = Path("day16.txt").read_text().split("\n\n")
my_ticket = my_ticket.split("\n")[1]
nearby_tickets = nearby_tickets.strip().split("\n")[1:]


def valid_range(rules):
    allowed_ranges = []
    for rule in rules.split():
        if pat := re.match("([0-9]+)-([0-9]+)$", rule):
            min, max = pat.groups()
            allowed_ranges.append((int(min), int(max)))
    return allowed_ranges


def value_in_ranges(value, ranges):
    return any(min <= value <= max for min, max in ranges)


def error_rate(valid_ranges, nearby_tickets):
    invalid_values = 0
    for ticket in nearby_tickets:
        ticket_values = [int(v) for v in ticket.split(",")]
        for value in ticket_values:
            if not value_in_ranges(value, valid_ranges):
                invalid_values += value
    return invalid_values


def filter_tickets(valid_ranges, nearby_tickets):
    valid_ones = []
    for ticket in nearby_tickets:
        ticket_values = [int(v) for v in ticket.split(",")]
        if all(value_in_ranges(value, valid_ranges) for value in ticket_values):
            valid_ones.append(ticket_values)
    return valid_ones


def find_order(rules, nearby_tickets):
    rules_dict = {}
    for rule in rules.strip().split("\n"):
        rulename, rulevalue = rule.split(":")
        rules_dict[rulename] = valid_range(rulevalue)
    possibilities = [set(rules_dict.keys()) for _ in range(len(nearby_tickets[0]))]
    for ticket in nearby_tickets:
        for i, (ticket_value, rulenames) in enumerate(zip(ticket, possibilities)):
            to_remove = set()
            for rulename in rulenames:
                if not value_in_ranges(ticket_value, rules_dict[rulename]):
                    print(f"Removing {rulename} from field {i}")
                    to_remove.add(rulename)
            rulenames -= to_remove
    for _ in range(len(nearby_tickets[0])):
        # If a column is known, it can't also be a possibility in another column
        known = [(i, col) for i, col in enumerate(possibilities) if len(col) == 1]
        for i, col in enumerate(possibilities):
            for k, known_set in known:
                if i != k:
                    col -= known_set
        print(known)
    columns = [p.pop() for p in possibilities]
    columns_ids_for_part2 = [
        i for i, name in enumerate(columns) if name.startswith("departure")
    ]
    my_ticket_values = [int(i) for i in my_ticket.split(",")]
    print(columns_ids_for_part2, my_ticket_values)
    return reduce(mul, [my_ticket_values[i] for i in columns_ids_for_part2], 1)


print("Part 1:", error_rate(valid_range(rules), nearby_tickets))
print("Part 2:", find_order(rules, filter_tickets(valid_range(rules), nearby_tickets)))
