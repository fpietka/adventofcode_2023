import re

from dataclasses import dataclass

lines = open('input_02', 'r')
games = lines.readlines()


@dataclass
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0

    def parse(self, draw_line):
        for color_line in draw_line.split(', '):
            amount, color = color_line.split(' ')
            color = color.replace('\n', '')
            amount = int(amount)

            if color == 'red' and amount > self.red:
                self.red = amount
            elif color == 'green' and amount > self.green:
                self.green = amount
            elif color == 'blue' and amount > self.blue:
                self.blue = amount

    def get_power(self):
        return self.red * self.green * self.blue

total = 0
power = 0

red = 12
green = 13
blue = 14

all_games = {}
for game in games:
    game_id = int(re.search(r'^Game (\d+):', game).group(1))
    colors = game[game.find(': ') + 2:]
    draws = colors.split('; ')

    my_draw = Draw()
    for draw in draws:
        my_draw.parse(draw)

    # part 2
    power += my_draw.get_power()

    # part 1
    if my_draw.red <= red and my_draw.green <= green and my_draw.blue <= blue:
        total += game_id

print(total)
print(power)
