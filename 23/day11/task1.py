from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = True

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

space = []

for line in lines:
    space.append(list(line))
    if '#' not in line:
        space.append(list(line))

rotated_space = list(zip(*space[::-1]))
space = []
for line in rotated_space:
    space.append(line)
    if '#' not in line:
        space.append(line)

rotated_space = list(zip(*space[::-1]))
rotated_space = list(zip(*rotated_space[::-1]))
space = list(zip(*rotated_space[::-1]))

# pprint(space)

galaxies = set()
for y in range(len(space)):
    for x in range(len(space[0])):
        if space[y][x] == '#':
            galaxies.add((x, y))

# print(galaxies)


def calc_cart_dist(cord1, cord2):
    return abs(cord2[0] - cord1[0]) + abs(cord2[1] - cord1[1])


dist_sum = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            dist_sum += calc_cart_dist(galaxy1, galaxy2)

print(dist_sum//2)
