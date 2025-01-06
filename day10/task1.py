from math import ceil
from os import path

from day10.field import Field

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

pipe_maze = Field(maze=[[*line] for line in lines])

result = pipe_maze.solve()
pipe_maze.print_solution()

current_node = pipe_maze.last_checked_node
pipe_path = []
while current_node.parent is not None:
    pipe_path.append(current_node)
    current_node = current_node.parent

# print('pipe_path:')
# for node in pipe_path:
#     print(str(node))
print(f'Furthest position: {ceil((len(pipe_path)) / 2)}')
print(pipe_path[ceil((len(pipe_path)) / 2)])
