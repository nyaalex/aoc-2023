from advent import AdventDay


class Day2(AdventDay):

    def __init__(self):
        super().__init__(2023, 2)

    def part_1(self):
        total = 0
        for game in self.read_lines():
            game_id, rounds = game.split(': ')
            game_id = int(game_id[5:])
            is_possible = True

            for game_round in rounds.split('; '):

                for colour in game_round.split(', '):
                    count, colour = colour.split(' ')
                    count = int(count)
                    if (count > 12 and colour == 'red') or \
                            (count > 13 and colour == 'green') or \
                            (count > 14 and colour == 'blue'):
                        is_possible = False
                        break
                if not is_possible:
                    break

            if is_possible:
                total += game_id

        return total

    def part_2(self):
        total = 0
        for game in self.read_lines():
            game_id, rounds = game.split(': ')
            game_id = int(game_id[5:])
            game_min = {'red': 0, 'green': 0, 'blue': 0}

            for game_round in rounds.split('; '):
                for colour in game_round.split(', '):
                    count, colour = colour.split(' ')
                    count = int(count)

                    game_min[colour] = max(count, game_min[colour])
            power = game_min['red'] * game_min['green'] * game_min['blue']
            total += power

        return total


if __name__ == '__main__':
    d2 = Day2()
    d2.main()
