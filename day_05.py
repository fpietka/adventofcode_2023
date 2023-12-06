lines = open('input_05', 'r')

seeds = []
seeds_ranges = new_seeds_ranges = []
processed = []
processed_ranges = []

def build(entry, source):
    before = into = after = None

    if entry[0] < source[0]:
        before = (
            entry[0],
            min(entry[1], source[0] - 1)
        )

    if (
        source[0] >= entry[0] and source[0] <= entry[1]
        or source[1] >= entry[0] and source[1] <= entry[1]
        or (
            entry[0] >= source[0] and entry[0] <= source[1]
            and entry[1] >= source[0] and entry[1] <= source[1]
        )
    ):
        into = (
            max(entry[0], source[0]),
            min(entry[1], source[1])
        )

    if entry[1] > source[1]:
        after = (
            max(entry[0], source[1] + 1),
            entry[1]
        )

    return before, into, after


for line in lines.readlines():
    line = line.replace("\n", '')
    if not seeds:
        # do both seeds and range
        seeds = [int(seed) for seed in line.split(' ')[1:]]

        straight_list = line.split(' ')[1:]
        seeds_ranges = [(int(straight_list[i]), int(straight_list[i]) + int(straight_list[i+1])) for i in range(0, len(straight_list), 2)]
        continue

    if not line:
        continue
    elif line[-4:-1] == 'map':
        processed = []
        if new_seeds_ranges:
            for index, _ in enumerate(seeds_ranges):
                if index not in processed_ranges:
                    # re-add unprocessed seeds for next round
                    new_seeds_ranges.append(seeds_ranges[index])
            seeds_ranges = new_seeds_ranges
            processed_ranges = []
            new_seeds_ranges = []
    else:
        parts = [int(part) for part in line.split(' ')]
        dest_start = parts[0]
        source_start, source_end = parts[1], parts[1] + parts[2]

        # part 1
        for index, seed in enumerate(seeds):
            if seed >= source_start and seed <= source_end and index not in processed:
                seeds[index] = dest_start + seed - source_start
                processed.append(index)

        # part 2
        transformation = dest_start - source_start
        for index, range_ in enumerate(seeds_ranges):

            if index not in processed_ranges:
                before, into, after = build(range_, (source_start, source_end))
                if into:
                    new_seeds_ranges.append((into[0] + transformation, into[1] + transformation))
                    processed_ranges.append(index)
                    if before:
                        new_seeds_ranges.append(before)
                    if after:
                        new_seeds_ranges.append(after)
                # else not processed

print(min(seeds))

# 40645637 too high
print(min([seed for seed, _ in seeds_ranges]))
