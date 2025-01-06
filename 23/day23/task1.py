from os import path

from day23.solve import Astar

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")

maze = Astar(f.read())
# maze.solve_step_by_step()
maze.solve()
# maze.print_solution()
print(len(maze.solution_path) + 1)
f.close()
