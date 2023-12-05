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

# Parse ranges to list
for i in range(0, len(inputs), 2):
    seeds.append((int(inputs[i]), int(inputs[i]) + int(inputs[i + 1])))

old_category = seeds   # First categeroy

# Looping through Category maps
for mapping in mappings:
    _, *ranges = mapping.splitlines()  # Removes starting text
    ranges = [list(map(int, r.split())) for r in ranges]  # Parse ranges to list after converting to int
    new_category = []

    # Continue looping till all seed ranges are used
    while len(old_category) > 0:
        # print(f'old category:{old_category}')
        lower, upper = old_category.pop()
        for destination, source, _range in ranges:
            overlapping_lower = max(lower, source)  # Overlapping lower
            overlapping_upper = min(upper, source + _range)  # Overlapping upper
            if overlapping_lower < overlapping_upper:
                new_category.append((overlapping_lower - source + destination, overlapping_upper - source + destination))  # Add overlapping range to next category
                if overlapping_lower > lower:
                    old_category.append((lower, overlapping_lower))  # Add left outer range to old_category ranges
                if upper > overlapping_upper:
                    old_category.append((overlapping_upper, upper))  # Add right outer range to old_category ranges
                break
        else:
            new_category.append((lower, upper))
    old_category = new_category
    # print(f'new category:{old_category}')
    # print('-------------------')

print(f'lowest location: {min(old_category)[0]}')
