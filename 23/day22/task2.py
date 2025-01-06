from copy import deepcopy
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()


def print_faces(grid):
    grid = grid[::-1]
    # print x z
    for z in range(max_z + 1):
        for x in range(max_x + 1):
            layer = [grid[z][y][x] for y in range(max_y + 1)]
            if not all(xx == '.' for xx in layer):
                layer = list(filter(lambda xx: xx != '.', layer))
                print(layer[0] if len(set(layer)) == 1 else '?', end=' ')
            else:
                print('.', end=' ')
        print()

    print('-----------')

    # print y z
    for z in range(max_z + 1):
        for y in range(max_y + 1):
            layer = [grid[z][y][x] for x in range(max_x + 1)]
            if not all(xx == '.' for xx in layer):
                layer = list(filter(lambda xx: xx != '.', layer))
                print(layer[0] if len(set(layer)) == 1 else '?', end=' ')
            else:
                print('.', end=' ')
        print()

    print('-----------')


def print_layers(grid):
    for z in range(max_z + 1):
        for yy in range(max_y + 1):
            for xx in range(max_x + 1):
                print(grid[z][yy][xx], end=' ')
            print()
        print('|||||||||||||||')


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

stack = [[['.' if z != 0 else '-' for _ in range(max_x + 1)] for _ in range(max_y + 1)] for z in range(max_z + 1)]

# pprint(stack)

for index, brick in enumerate(bricks):
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    for z in range(z1, z2 + 1):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                stack[z][y][x] = '#'  # chr(index + 65)

# pprint(stack)
bricks.sort(key=lambda p: p[0][2])


def check_drop(get_line, z):
    drop_count = 0
    below = get_line(z - 1 + drop_count)
    while all(xx == '.' for xx in below) and not all(xx == '-' for xx in below):
        drop_count -= 1
        below = get_line(z - 1 + drop_count)
    return drop_count


def drop(grid, skip=None):
    global bricks
    copy_bricks = deepcopy(bricks)
    count = -1
    total = 0
    while count != 0:
        new_bricks = []
        count = 0
        for i, b in enumerate(copy_bricks):
            old_x1, old_y1, old_z1 = b[0]
            old_x2, old_y2, old_z2 = b[1]
            drop_count = 0
            if b == skip:
                continue
            if old_x1 == old_x2 and old_y1 == old_y2 and old_z1 == old_z2:
                get_below = lambda n: [grid[n][old_y1][old_x1]]
                drop_count = check_drop(get_below, old_z1)
            if old_x1 != old_x2:
                get_below = lambda n: [grid[n][old_y1][xxx] for xxx in range(old_x2 - old_x1 + 1)]
                drop_count = check_drop(get_below, old_z1)
            if old_y1 != old_y2:
                get_below = lambda n: [grid[n][yyy][old_x1] for yyy in range(old_y2 - old_y1 + 1)]
                drop_count = check_drop(get_below, old_z1)
            if old_z1 != old_z2:
                get_below = lambda n: [grid[n][old_y1][old_x1]]
                drop_count = check_drop(get_below, old_z1)
            if drop_count != 0:
                for zz in range(old_z1, old_z2 + 1):
                    for yy in range(old_y1, old_y2 + 1):
                        for xx in range(old_x1, old_x2 + 1):
                            grid[zz][yy][xx] = '.'
                for zz in range(old_z1 + drop_count, old_z2 + drop_count + 1):
                    for yy in range(old_y1, old_y2 + 1):
                        for xx in range(old_x1, old_x2 + 1):
                            grid[zz][yy][xx] = str(i)
                new_bricks.append(((old_x1, old_y1, old_z1 + drop_count), (old_x2, old_y2, old_z2 + drop_count)))
                count += 1
                total += 1
            else:
                for zz in range(old_z1, old_z2 + 1):
                    for yy in range(old_y1, old_y2 + 1):
                        for xx in range(old_x1, old_x2 + 1):
                            grid[zz][yy][xx] = str(i)
                new_bricks.append(((old_x1, old_y1, old_z1), (old_x2, old_y2, old_z2)))
        copy_bricks = new_bricks
        copy_bricks.sort(key=lambda p: p[0][2])
    if skip is None:
        bricks = copy_bricks
    return total


# print_faces(deepcopy(stack))
drop(stack)
print_faces(deepcopy(stack))


# print(bricks)

# print_layers(deepcopy(stack))


def disintegrate(grid):
    global bricks
    count = 0
    for i, b in enumerate(bricks):
        xd1, yd1, zd1 = b[0]
        xd2, yd2, zd2 = b[1]
        grid_copy = deepcopy(grid)
        for zz in range(zd1, zd2 + 1):
            for yy in range(yd1, yd2 + 1):
                for xx in range(xd1, xd2 + 1):
                    grid_copy[zz][yy][xx] = '.'
        dropped = drop(grid_copy, b)
        # print(i, dropped, b)
        if dropped != 0:
            count += dropped
        # if dropped:
        # for ii, bb in enumerate(bricks):
        #     if b == bb:
        #         continue
        #     old_x1, old_y1, old_z1 = bb[0]
        #     old_x2, old_y2, old_z2 = bb[1]
        #     drop_count = 0
        #     if old_x1 == old_x2 and old_y1 == old_y2 and old_z1 == old_z2:
        #         get_below = lambda z: [grid_copy[z][old_y1][old_x1]]
        #         drop_count = check_drop(get_below, old_z1)
        #     if old_x1 != old_x2:
        #         get_below = lambda z: [grid_copy[z][old_y1][xxx] for xxx in range(old_x2 - old_x1 + 1)]
        #         drop_count = check_drop(get_below, old_z1)
        #     if old_y1 != old_y2:
        #         get_below = lambda z: [grid_copy[z][yyy][old_x1] for yyy in range(old_y2 - old_y1 + 1)]
        #         drop_count = check_drop(get_below, old_z1)
        #     if old_z1 != old_z2:
        #         get_below = lambda z: [grid_copy[z][old_y1][old_x1]]
        #         drop_count = check_drop(get_below, old_z1)
        #     if drop_count != 0:
        #         break
        # else:
        #     count += 1
        #     # print(i)

    print('ans: ', count)


bricks.sort(key=lambda p: p[0][2])

disintegrate(deepcopy(stack))

import collections as C, re


def drop(stack, skip=None):
    peaks = C.defaultdict(int)
    falls = 0

    for i, (u, v, w, x, y, z) in enumerate(stack):
        if i == skip: continue

        area = [(a, b) for a in range(u, x + 1)
                for b in range(v, y + 1)]
        peak = max(peaks[a] for a in area) + 1
        for a in area: peaks[a] = peak + z - w

        stack[i] = (u, v, peak, x, y, peak + z - w)
        falls += peak < w

    return not falls, falls


stack = sorted([[*map(int, re.findall(r'\d+', l))]
                for l in open('input.txt')], key=lambda b: b[2])

# drop(stack)
#
# print(*map(sum, zip(*[drop(stack.copy(), skip=i)
#                       for i in range(len(stack))])))
