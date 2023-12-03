import re

lines = open('input_03', 'r')

part_sum = 0

not_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

# build engine matrix
engine = []
for line in lines.readlines():
    engine.append(line)

pattern = r'\d+'
for line_number, engine_line in enumerate(engine, start=1):
    # get potential part numbers
    for match in [m for m in re.finditer(pattern, engine_line)]:
        # test char isnt a dot before or after the match
        if match.start() > 0:
            before = engine_line[match.start() - 1]
            if before not in not_symbols:
                part_sum += int(match.group(0))
                continue
        if match.end() < len(engine_line) - 1:
            after = engine_line[match.end()]
            if after not in not_symbols:
                part_sum += int(match.group(0))
                continue

        # test up/down taking into account diagonals
        if line_number > 1:
            line_above = engine[line_number -2][max(0, match.start() - 1):min(len(engine_line) - 1, match.end() + 1)]
            above = line_above.translate({ord(x): '' for x in not_symbols})
            if len(above) > 0:
                part_sum += int(match.group(0))
                continue
        if line_number < len(engine):
            line_below = engine[line_number][max(0, match.start() - 1):min(len(engine_line) - 1, match.end() + 1)]
            below = line_below.translate({ord(x): '' for x in not_symbols})
            if len(below) > 0:
                part_sum += int(match.group(0))
                continue

print(part_sum)

# part 2

part_sum = 0
multipliers = {}

for line_number, engine_line in enumerate(engine, start=1):
    # get potential part numbers
    for match in [m for m in re.finditer(pattern, engine_line)]:
        # test char isnt a dot before or after the match
        if match.start() > 0:
            before = engine_line[match.start() - 1]
            if before == '*':
                my_key = (line_number, match.start() - 1)
                if my_key in multipliers.keys():
                    multipliers[my_key].append(int(match.group(0)))
                else:
                    multipliers[my_key] = [int(match.group(0))]
                continue
        if match.end() < len(engine_line) - 1:
            after = engine_line[match.end()]
            if after == '*':
                my_key = (line_number, match.end())
                if my_key in multipliers.keys():
                    multipliers[my_key].append(int(match.group(0)))
                else:
                    multipliers[my_key] = [int(match.group(0))]
                continue

        # test up/down taking into account diagonals
        if line_number > 1:
            line_above = engine[line_number -2][max(0, match.start() - 1):min(len(engine_line) - 1, match.end() + 1)]
            above = line_above.translate({ord(x): '' for x in not_symbols})
            if above == '*':
                my_key = (line_number -1, max(0, match.start() - 1) + line_above.find('*'))
                if my_key in multipliers.keys():
                    multipliers[my_key].append(int(match.group(0)))
                else:
                    multipliers[my_key] = [int(match.group(0))]
                continue
        if line_number < len(engine):
            line_below = engine[line_number][max(0, match.start() - 1):min(len(engine_line) - 1, match.end() + 1)]
            below = line_below.translate({ord(x): '' for x in not_symbols})
            if below == '*':
                my_key = (line_number +1, max(0, match.start() - 1) + line_below.find('*'))
                if my_key in multipliers.keys():
                    multipliers[my_key].append(int(match.group(0)))
                else:
                    multipliers[my_key] = [int(match.group(0))]
                continue

for multiplier in multipliers.values():
    if len(multiplier) == 2:
        part_sum += multiplier[0] * multiplier[1]

print(part_sum)


# part 1: 544664

# part 2:
# when a part has a "*" surrounding it, we need to know if another part has it too

"""

match: no symbol -> discard
       symbol except * -> add
       symbol * -> keep for later
later: get matches having * -> do they share a symbol

"""
