from copy import deepcopy
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = True

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

# print(lines)
bricks = []
max_x = 0
max_y = 0
max_z = 0

for line in lines:
    x1, y1, z1 = [int(n) for n in line.split('~')[0].split(',')]
    x2, y2, z2 = [int(n) for n in line.split('~')[1].split(',')]
    bricks.append(((x1, y1, z1), (x2, y2, z2)))
    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)
    max_z = max(max_z, z1, z2)

stack = [[['.' if z != 0 else '-' for x in range(max_x + 1)] for y in range(max_y + 1)] for z in range(max_z + 1)]

# pprint(stack)

for index, brick in enumerate(bricks):
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    for z in range(z1, z2 + 1):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                stack[z][y][x] = chr(index + 65)


# pprint(stack)


def print_faces(grid):
    grid = grid[::-1]
    # print x z
    for z in range(max_z + 1):
        for x in range(max_x + 1):
            face = ''.join([grid[z][y][x] for y in range(max_y + 1)]).replace('.', '')
            print(face[0] if face != '' else '.', end=' ')
        print()

    print('-----------')

    # print y z
    for z in range(max_z + 1):
        for y in range(max_y + 1):
            face = ''.join([grid[z][y][x] for x in range(max_x + 1)]).replace('.', '')
            print(face[0] if face != '' else '.', end=' ')
        print()


def print_layers(grid):
    grid = grid

    for z in range(max_z + 1):
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                print(grid[z][y][x], end=' ')
            print()
        print('|||||||||||||||')


# print_faces(deepcopy(stack))
print_layers(deepcopy(stack))

# data = np.array([[1, 2, 3], #14 (corner1)
#                  [4, 5, 6], #77 (corner2)
#                  [2.5, 3.5, 4.5], #38.75 (duplicated pixel)
#                  [2.9, 3.9, 4.9], #47.63 (duplicated pixel)
#                  [1.5, 2, 3]]) #15.25 (one step up from [1, 2, 3])
# step = 0.5
# data_idx = ((data - data.min(axis=0))//step).astype(int)
# M = np.zeros(np.max(data_idx, axis=0) + 1)
# x, y, z = data_idx.T
# M[x, y, z] = F
