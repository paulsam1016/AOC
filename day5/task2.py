from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
inputs, *mappings = f.read().split('\n\n')

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
