from os import path

from day10.field import Field

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = True

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

pipe_maze = Field(maze=[[*line] for line in lines])

result = pipe_maze.solve()
pipe_maze.print_enclosed_solution()

current_node = pipe_maze.last_checked_node
pipe_path = []
while current_node.parent is not None:
    pipe_path.append(current_node.position)
    current_node = current_node.parent

# print('pipe_path:')
# for node in pipe_path:
#     print(str(node))

part2 = 0
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if (x, y) in pipe_path:
            continue
        # Point a ray in one direction
        # Main idea is to count crossing with vertical bars
        # But we need to consider corners that cancel each other out:
        #    - LJ for the top horizontal parity (line will stay at the top)
        #    - F7 for the bottom horizontal parity (line will stay at the bottom)
        par_bottom = par_top = 0
        for ny in range(y + 1):
            if (x, ny) in pipe_path and lines[x][ny] in "|JL":
                par_top ^= 1
            if (x, ny) in pipe_path and lines[x][ny] in "|F7":
                par_bottom ^= 1
        if par_bottom and par_top:
            part2 += 1

print(part2)
