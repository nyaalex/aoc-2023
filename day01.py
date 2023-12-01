import re

from advent import AdventDay

# The explanation here is that two numbers can overlap, e.g. twone, and the part two function just subs out string
# matches for numeric counterparts. By adding any overlaps back in we can ensure no digit gets mangled part way through
# substitution
DIGITS = [
    ('one', 'o1e'),
    ('two', 't2o'),
    ('three', 't3e'),
    ('four', '4'),
    ('five', '5e'),
    ('six', '6'),
    ('seven', '7n'),
    ('eight', 'e8t'),
    ('nine', 'n9e')
]

class Day1(AdventDay):

    def __init__(self):
        super().__init__(2023, 1)

    def part_1(self):
        total = 0
        for line in self.read_lines():
            digits = re.findall('\\d', line)
            n = int(digits[0] + digits[-1])
            total += n
        return total

    def part_2(self):
        total = 0
        for line in self.read_lines():
            for s, r in DIGITS:
                line = re.sub(s, r, line)
            digits = re.findall('\\d', line)
            n = int(digits[0] + digits[-1])
            total += n
        return total


if __name__ == '__main__':
    d1 = Day1()
    d1.main()
