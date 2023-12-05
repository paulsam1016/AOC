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

    for mapping in mappings:
        _, *ranges = mapping.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        for d, s, r in ranges:
            if s <= data < s + r:
                data = data + d - s
                break
    seedLocations[seed] = data

# print(f'seedLocations : {seedLocations}')

# print(f'lowest location seed: {min(seedLocations, key=seedLocations.get)}')
print(f'lowest location : {seedLocations[min(seedLocations, key=seedLocations.get)]}')
