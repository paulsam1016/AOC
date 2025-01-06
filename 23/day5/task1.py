from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
seeds, *mappings = f.read().split('\n\n')

seeds = seeds.split(': ')[1].split()
seedLocations = {}

# print(data)

for seed in seeds:
    data = int(seed)
    categoryNumbers = [data]

    # Looping through Category maps
    for mapping in mappings:
        _, *ranges = mapping.splitlines()  # Removes starting text
        ranges = [list(map(int, r.split())) for r in ranges]  # Parse ranges to list after converting to int
        for d, s, r in ranges:
            if s <= data < s + r:   # Map based on source and destination
                data = data + d - s
                categoryNumbers.append(data)
                break
        else:   # No mapping, so same
            categoryNumbers.append(data)
    seedLocations[seed] = data
    # print('Seed {}, soil {}, fertilizer {}, water {}, light {}, temperature {}, humidity {}, location {}.'.format(*categoryNumbers))
# print(f'seedLocations : {seedLocations}')
# print(f'lowest location seed: {min(seedLocations, key=seedLocations.get)}')
print(f'lowest location : {seedLocations[min(seedLocations, key=seedLocations.get)]}')
