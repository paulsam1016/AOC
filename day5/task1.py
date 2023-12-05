from os import path

location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
seeds, *mappings = f.read().split('\n\n')

# ex = '''seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4'''
#
# seeds, *mappings = ex.split('\n\n')

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

print(f'seedLocations : {seedLocations}')

print(f'lowest location seed: {min(seedLocations, key=seedLocations.get)}')
print(f'lowest location : {seedLocations[min(seedLocations, key=seedLocations.get)]}')
