codes = open('input_06', 'r')
lines = codes.readlines()


race_durations = [int(duration) for duration in lines[0].split(' ')[1:] if duration]
race_records = [int(record) for record in lines[1].split(' ')[1:] if record]

speed = 1
def accel(race_duration=0, record=0):
    result = 0
    for x in range(race_duration):
        if ((x * speed) * (race_duration - x)) > record:
            result += 1
    return result

total = 0

for index, race_duration in enumerate(race_durations):
    better = accel(race_duration=race_duration, record=race_records[index])
    if total:
        total *= better
    else:
        total = better

print(total)

# part 2
race_duration = int(lines[0].split(':')[1].replace(' ', ''))
race_record = int(lines[1].split(':')[1].replace(' ', ''))

print(accel(race_duration=race_duration, record=race_record))
