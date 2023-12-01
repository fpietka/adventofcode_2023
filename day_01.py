import re

codes = open('input_01', 'r')
lines = codes.readlines()

# part 1
total = 0
for line in lines:
    chars = [char for char in line if char.isdigit()]
    number = int(chars[0] + chars[-1])
    total += number

print(total)

# part 2
char_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

total = 0
for line in lines:
    chars = []
    for index in range(len(line)):
        match = re.search(r'|'.join(char_numbers.keys()), line[index:])
        if match:
            chars.append(match.group(0))

    number = int(char_numbers[chars[0]] + char_numbers[chars[-1]])
    total += number

print(total)
