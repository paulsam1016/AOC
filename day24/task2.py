from os import path

import sympy

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

# print(lines)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []
answer = []

for i, line in enumerate(lines):
    pos, v = [tuple(map(int, x.split(', '))) for x in line.split(' @ ')]
    equations.append((xr - pos[0]) * (v[1] - vyr) - (yr - pos[1]) * (v[0] - vxr))
    equations.append((yr - pos[1]) * (v[2] - vzr) - (zr - pos[2]) * (v[1] - vyr))
    if i < 2:
        continue
    answers = [solution for solution in sympy.solve(equations) if all(value % 1 == 0 for value in solution.values())]
    if len(answers) == 1:
        break

answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])
print(i)
