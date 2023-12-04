import re


lines = open('input_04', 'r')

# part 1
def geometric_progression(n):
    return 1 * (2 ** (n - 1))

total = 0
sc_total = 0
scratchcards = [dict({'value': 0, 'amount': 1}) for _ in range(len(lines.readlines()))]

lines = open('input_04', 'r')
for index, line in enumerate(lines.readlines()):
    winning, numbers = line.split(': ')[1].split(' | ')

    winning_set = set([int(x) for x in re.split(r'\s+', winning.strip())])
    number_set = set([int(x) for x in re.split(r'\s+', numbers.strip())])

    good = len(winning_set.intersection(number_set))
    scratchcards[index]['value'] = good
    if good > 0:
        total += geometric_progression(good)

    for _ in range(1, scratchcards[index]['amount'] + 1):
        for next_index in range(1, good + 1):
            scratchcards[index + next_index]['amount'] += 1
    sc_total += scratchcards[index]['amount']


print(total)

print(sc_total)
