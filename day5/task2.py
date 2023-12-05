from os import path

location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
inputs, *mappings = f.read().split('\n\n')

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
# inputs, *mappings = ex.split('\n\n')

inputs = inputs.split(': ')[1].split()
seeds = []

# print(data)

for i in range(0, len(inputs), 2):
    seeds.append((int(inputs[i]), int(inputs[i]) + int(inputs[i + 1])))

# seeds = [(79, 92)]

for mapping in mappings:
    _, *ranges = mapping.splitlines()
    ranges = [[int(x) for x in r.split()] for r in ranges]
    new = []
    while len(seeds) > 0:
        # print(f'seeds:{seeds}')
        lower, upper = seeds.pop()
        for destination, source, _range in ranges:
            outer_lower = max(lower, source)
            outer_upper = min(upper, source + _range)
            if outer_lower < outer_upper:
                new.append((outer_lower - source + destination, outer_upper - source + destination))
                if outer_lower > lower:
                    seeds.append((lower, outer_lower))
                if upper > outer_upper:
                    seeds.append((outer_upper, upper))
                break
        else:
            new.append((lower, upper))
    seeds = new
    # print(f'new seeds:{seeds}')
    # print('-------------------')

print(f'lowest location: {min(seeds)[0]}')
