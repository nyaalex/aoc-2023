from advent import AdventDay
import re

DIGITS = '0123456789'
SYMBOLS = "#%&*+-/=@$"


class Day3(AdventDay):

    def __init__(self):
        super().__init__(2023, 3)

    def is_part_num_valid(self, span, line):

        g = self.read_lines()
        max_x, max_y = len(g[0]) - 1, len(g) - 1

        start, end = span
        start = max(start - 1, 0)
        end = min(end + 1, max_x)

        for x in range(start, end):
            for y in range(max(line - 1, 0), min(line + 2, max_y)):
                if g[y][x] in SYMBOLS:
                    return True

    def part_1(self):
        total = 0
        for y, line in enumerate(self.read_lines()):
            for match in re.finditer('\\d+', line):
                num = int(match.group(0))
                if self.is_part_num_valid(match.span(), y):
                    total += num

        return total

    def get_gear_ratio(self, x, y):
        g = self.read_lines()

        part_nums = []
        for line in g[max(y - 1, 0): min(y + 2, len(g))]:
            for m in re.finditer('\\d+', line):
                start, end = m.span()
                if x in range(start - 1, end + 1):
                    part_nums.append(int(m.group(0)))

        if len(part_nums) != 2:
            return 0
        else:
            return part_nums[0] * part_nums[1]

    def part_2(self):
        total = 0
        for y, line in enumerate(self.read_lines()):
            for match in re.finditer('\\*', line):
                x = match.span()[0]
                total += self.get_gear_ratio(x, y)
        return total


if __name__ == '__main__':
    d3 = Day3()
    d3.main()
