from advent import AdventDay

NUM_COUNT = 10


class Day4(AdventDay):

    def __init__(self):
        super().__init__(2023, 4)

    def part_1(self):
        total = 0
        for card in self.parse_ints():
            winning_numbers = set(card[1:NUM_COUNT + 1])
            winning_numbers &= set(card[NUM_COUNT + 1:])
            if winning_numbers:
                total += (1 << len(winning_numbers) - 1)
        return total

    def part_2(self):
        card_counts = [1] * NUM_COUNT

        total = 0
        for card in self.parse_ints():
            winning_numbers = set(card[1:NUM_COUNT + 1])
            winning_numbers &= set(card[NUM_COUNT + 1:])

            curr_count = card_counts.pop(0)
            total += curr_count

            card_counts.append(1)
            for i in range(len(winning_numbers)):
                card_counts[i] += curr_count

        return total


if __name__ == '__main__':
    d4 = Day4()
    d4.main()
