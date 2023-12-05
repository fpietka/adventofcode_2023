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

        dest_range = list(range(parts[0], parts[0] + parts[2]))
        source_range = list(range(parts[1], parts[1] + parts[2]))
        for index, seed in enumerate(seeds):
            if seed in source_range and index not in processed:
                seeds[index] = dest_range[source_range.index(seed)]
                processed.append(index)

print(min(seeds))
