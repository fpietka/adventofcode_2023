lines = open('input_05', 'r')

seeds = []
processed = []

for line in lines.readlines():
    line = line.replace("\n", '')
    if not seeds:
        seeds = [int(seed) for seed in line.split(' ')[1:]]
    elif not line:
        continue
    elif line[-4:-1] == 'map':
        processed = []
    else:
        parts = [int(part) for part in line.split(' ')]
        dest_start = parts[0]
        source_start, source_end = parts[1], parts[1] + parts[2]
        for index, seed in enumerate(seeds):
            if seed >= source_start and seed <= source_end and index not in processed:
                seeds[index] = dest_start + seed - source_start
                processed.append(index)

print(min(seeds))
