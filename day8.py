from collections import Counter
from pathlib import Path

class Machine:
    def __init__(self, code):
        self.code = list(self.parse(code))
        self.seen = Counter()
        self.ip = 0
        self.acc = 0

    def parse(self, code):
        for line in code.split("\n"):
            if not line:
                continue
            op, arg = line.split()
            yield op, int(arg)

    def run(self):
        while True:
            op, arg = self.code[self.ip]
            if self.seen[self.ip]:
                raise ValueError(f"{self.ip=} already seen, {self.acc=}")
            self.seen[self.ip] += 1
            getattr(self, "do_" + op)(arg)

    def do_nop(self, arg):
        self.ip += 1

    def do_acc(self, arg):
        self.acc += arg
        self.ip += 1

    def do_jmp(self, arg):
        self.ip += arg


# part 1
try:
    Machine(Path("day8.txt").read_text()).run()
except ValueError as err:
    print(err)

# part 2
code = Path("day8.txt").read_text().strip().split("\n")
for i in range(len(code)):
    test = code.copy()
    if test[i].startswith("acc"):
        continue
    if test[i].startswith("jmp"):
        test[i] = "nop" + test[i][3:]
    elif test[i].startswith("nop"):
        test[i] = "jmp" + test[i][3:]
    try:
        m = Machine("\n".join(test))
        m.run()
    except ValueError:
        pass
    except IndexError:
        if m.ip == len(code):
            print(f"Fixed line {i}, got: {m.acc=}")
