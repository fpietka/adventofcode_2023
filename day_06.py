codes = open('input_06', 'r')
lines = codes.readlines()


race_durations = [int(duration) for duration in lines[0].split(' ')[1:] if duration]
race_records = [int(record) for record in lines[1].split(' ')[1:] if record]

def accel(speedup=0, race_duration=0):
    speed = 0
    timeleft = race_duration
    distance = 0

    for duration in range(speedup):
        timeleft -= 1
        if timeleft == 0:
            # game over
            return
        speed += 1

    for duration in range(timeleft):
        distance += speed

    return distance

total = 0

for index, race_duration in enumerate(race_durations):
    better = 0
    for speedup_duration in range(race_duration):
        distance = accel(speedup=speedup_duration, race_duration=race_duration)
        if distance > race_records[index]:
            better += 1
    if total:
        total *= better
    else:
        total = better

print(total)

# part 2
race_duration = int(lines[0].split(':')[1].replace(' ', ''))
race_record = int(lines[1].split(':')[1].replace(' ', ''))

speed = 1
def accel2(race_duration=0, record=0):
    result = 0
    for x in range(race_duration):
        if ((x * speed) * (race_duration - x)) > record:
            result += 1
    return result

print(accel2(race_duration=race_duration, record=race_record))
