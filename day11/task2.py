from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

space = []
expansion = 1000000 - 1
x_expanders = []
y_expanders = []

for y, line in enumerate(lines):
    space.append(list(line))
    if '#' not in line:     # if expansions in y-axis append row index
        y_expanders.append(y)

rotated_space = list(zip(*space[::-1]))
for x, line in enumerate(rotated_space):
    if '#' not in line:     # if expansions in x-axis append column index
        x_expanders.append(x)

galaxies = []
for y in range(len(space)):
    for x in range(len(space[0])):
        if space[y][x] == '#':
            galaxies.append((x, y))

# print(galaxies)

for index, galaxy in enumerate(galaxies):
    # find expansions before galaxy
    x_expansions = expansion * len(list(filter(lambda x: x < galaxy[0], x_expanders)))
    y_expansions = expansion * len(list(filter(lambda y: y < galaxy[1], y_expanders)))
    # update galaxy location
    galaxies[index] = (galaxy[0] + x_expansions, galaxy[1] + y_expansions)


# print(set(galaxies))


def calc_cart_dist(cord1, cord2):
    return abs(cord2[0] - cord1[0]) + abs(cord2[1] - cord1[1])


dist_sum = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            dist_sum += calc_cart_dist(galaxy1, galaxy2)

print(dist_sum // 2)
