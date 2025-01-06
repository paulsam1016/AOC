from collections import deque
from copy import deepcopy
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/t.txt")
lines = f.read().splitlines()

plot = lines
total_steps = 26501365
starting_pos = ()
jumps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

temp_plot = []

for index, row in enumerate(plot):
    if 'S' in row:
        starting_pos = (index, row.find('S'))
    temp_plot.append(list(row.replace('S', '.')))

plot = temp_plot
size = len(plot)


# for row in plot:
#     print(''.join(row), end='\n')


def repeat_plot(plot_to_change):
    t_plot = []
    for i, r in enumerate(plot_to_change):
        temp_row = plot[i % size] + r + plot[i % size]
        t_plot.append(temp_row)
    t_plot = [r * (len(t_plot[0]) // size) for r in plot] + t_plot + [r * (len(t_plot[0]) // size) for r in plot]

    return t_plot


# o_tiles = deque([starting_pos])
# seen = {starting_pos}
# when_seen = [total_steps]
# copy_plot = deepcopy(plot)
# repeat = False
# for step in range(total_steps, 0, -1):
#     temp_o_tiles = []
#     if repeat:
#         repeat = False
#         copy_plot = repeat_plot(copy_plot)
#         o_tiles = deque([(o_tile[0] + size, o_tile[1] + size) for o_tile in o_tiles])
#         seen = {(seen_tile[0] + size, seen_tile[1] + size) for seen_tile in seen}
#     while o_tiles:
#         r, c = o_tiles.popleft()
#         for jump in jumps:
#             new_pos = (r + jump[0], c + jump[1])
#             # Check if plot is not in seen
#             if new_pos in seen:
#                 continue
#             # Check if plot is not rock
#             if copy_plot[new_pos[0]][new_pos[1]] == '#':
#                 continue
#             if new_pos[0] == (len(copy_plot) - 1) or new_pos[0] == 0 or new_pos[1] == (len(copy_plot) - 1) or new_pos[1] == 0:
#                 repeat = True
#             temp_o_tiles.append(new_pos)
#             seen.add(new_pos)
#             when_seen.append(step - 1)
#             copy_plot[new_pos[0]][new_pos[1]] = 'O'
#         copy_plot[r][c] = '.'
#     o_tiles = deque(temp_o_tiles)
#
#     # for row in copy_plot:
#     #     print(''.join(row), end='\n')
#
#     print(total_steps - step + 1, sum(x % 2 == 0 for x in when_seen))
#
# print(len(copy_plot) // size)

print(0.6802 * total_steps ** 2 + -3.0626 * total_steps + 9.2943)
print(0.6738 * total_steps ** 2 + -3.2541 * total_steps + 4.0547)


def do(get, start, t):
    bfs = {start}

    for _ in range(t):
        new_bfs = set()
        for i, j in bfs:
            new_bfs.add((i, j - 1))
            new_bfs.add((i, j + 1))
            new_bfs.add((i - 1, j))
            new_bfs.add((i + 1, j))
        new_bfs = {(i, j) for i, j in new_bfs if get(i, j) == "."}
        bfs = new_bfs

    return len(bfs)


grid = {(i, j): x for i, line in enumerate(lines) for j, x in enumerate(line)}
start = next(p for p, x in grid.items() if x == "S")
grid[start] = "."

print(size)
print(divmod(26501365, size))

get = lambda i, j: grid[i % size, j % size]

for n in range(4):
    print(total_steps % size + n * size, do(get, starting_pos, total_steps % size + n * size))

print(3916 + 15544 * 202300 + 15410 * 202300 ** 2)
