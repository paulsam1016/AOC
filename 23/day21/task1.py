from collections import deque
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = True

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

# print(lines)

plot = []
total_steps = 6
starting_pos = ()
jumps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = set()

for index, row in enumerate(lines):
    if 'S' in row:
        starting_pos = (index, row.find('S'))
    plot.append(list(row))

# print(plot)
# print(starting_pos)

seen = {starting_pos}
q = deque([(starting_pos[0], starting_pos[1], total_steps)])

while q:
    r, c, steps = q.popleft()
    if steps % 2 == 0:
        ans.add((r, c))
    if steps == 0:
        continue
    for jump in jumps:
        new_pos = (r + jump[0], c + jump[1])
        # Make sure within range
        if new_pos[0] > (len(plot) - 1) or new_pos[0] < 0 or new_pos[1] > (len(plot[0]) - 1) or new_pos[1] < 0:
            continue
        # Check if plot is not in seen
        if new_pos in seen:
            continue
        # Check if plot is not rock
        if plot[new_pos[0]][new_pos[1]] == '#':
            continue
        seen.add((new_pos[0], new_pos[1]))
        q.append((new_pos[0], new_pos[1], steps - 1))

print(len(ans))
