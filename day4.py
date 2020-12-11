from pathlib import Path
import re


def maybe_int(value):
    try:
        return int(value)
    except ValueError:
        return float("NaN")


required_rules = {
    "byr": lambda byr: 1920 <= maybe_int(byr) <= 2002,
    "iyr": lambda iyr: 2010 <= maybe_int(iyr) <= 2020,
    "eyr": lambda eyr: 2020 <= maybe_int(eyr) <= 2030,
    "hgt": lambda hgt: hgt.endswith("cm") and 150 <= maybe_int(hgt[:-2]) <= 193 or hgt.endswith("in") and 59 <= maybe_int(hgt[:-2]) <= 76,
    "hcl": re.compile("#[0-9a-f]{6}$").match,
    "ecl": lambda ecl: ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": re.compile("[0-9]{9}$").match
}


def check_passport(passport, strict=False):
    fields = dict(kvp.split(":") for kvp in passport.split())
    missing = set(required_rules.keys()) - set(fields.keys())
    if missing:
        return False
    if strict:
        for key, rule in required_rules.items():
            if not rule(fields[key]):
                return False
    return True


passports = Path("day4.txt").read_text().split("\n\n")
for strict in False, True:
    print(len([passport for passport in passports if check_passport(passport, strict)]))
