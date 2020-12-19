from pathlib import Path


class Rule:
    def __init__(self, rules):
        self.rules_dict = {}
        for line in rules.split("\n"):
            ruleno, rule = line.split(":")
            self.rules_dict[int(ruleno)] = self.parse_spec(rule.strip())

    def any(self, messages, rule):
        successes = []
        for tries in rule:
            successes.extend(self.all(messages, tries))
        return successes

    def all(self, messages, rules):
        if not rules or not messages:
            return messages
        rule_fct, rule_arg = self.rules_dict[rules[0]]
        return self.all(rule_fct(messages, rule_arg), rules[1:])

    def literal(self, messages, rule):
        return [message[1:] for message in messages if message.startswith(rule)]

    def match(self, message):
        rule_fct, rule_arg = self.rules_dict[0]
        messages = rule_fct([message], rule_arg)
        return any(message == "" for message in messages)

    def parse_spec(self, spec):
        if spec.startswith('"'):
            return self.literal, spec[1]
        elif "|" in spec:
            left, right = spec.split("|")
            return (
                self.any,
                (
                    [int(r) for r in left.strip().split()],
                    [int(r) for r in right.strip().split()],
                ),
            )
        else:
            return self.all, [int(r) for r in spec.strip().split()]


rules, messages = Path("day19.txt").read_text().split("\n\n")
r = Rule(rules.strip())
print("Part 1:", len([message for message in messages.split() if r.match(message)]))
r.rules_dict[8] = r.any, [(42, 8), (42,)]
r.rules_dict[11] = r.any, [(42, 11, 31), (42, 31)]
print("Part 2:", len([message for message in messages.split() if r.match(message)]))
