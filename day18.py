from pathlib import Path
import re


class NewMath:
    """Use @ as an addition operator with equal precedence with multiplication."""

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return NewMath(other.value * self.value)

    def __matmul__(self, other):
        return NewMath(other.value + self.value)

    def __repr__(self):
        return repr(self.value)

    @staticmethod
    def eval(operation):
        operation = operation.replace("+", "@")
        operation = re.sub("([0-9]+)", r"NewMath(\1)", operation)
        return eval(operation).value


class AdvancedNewMath:
    """This class inverts the semantic of + and *."""

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return AdvancedNewMath(other.value + self.value)

    def __add__(self, other):
        return AdvancedNewMath(other.value * self.value)

    def __repr__(self):
        return repr(self.value)

    @staticmethod
    def eval(operation):
        operation = re.sub(
            "([*+])", lambda match: "+" if match[0] == "*" else "*", operation
        )
        operation = re.sub("([0-9]+)", r"AdvancedNewMath(\1)", operation)
        return eval(operation).value


assert NewMath.eval("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert NewMath.eval("2 * 3 + (4 * 5)") == 26

print(
    "Part 1:",
    sum(
        NewMath.eval(line) for line in Path("day18.txt").read_text().strip().split("\n")
    ),
)

assert AdvancedNewMath.eval("1 + 2 * 3 + 4 * 5 + 6") == 231
assert AdvancedNewMath.eval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert AdvancedNewMath.eval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

print(
    "Part 2:",
    sum(
        AdvancedNewMath.eval(line)
        for line in Path("day18.txt").read_text().strip().split("\n")
    ),
)
