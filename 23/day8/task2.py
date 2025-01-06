import re
from itertools import cycle
from math import lcm
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
sequence, _, *inputs = f.read().splitlines()

# print(sequence)
# print(inputs)

network_map = {}
possible_nodes = []
ans = []

for _input in inputs:
    matches = re.findall('\w\w\w', _input)
    network_map[matches[0]] = {'L': matches[1], 'R': matches[2]}
    if matches[0][-1] == 'A':
        possible_nodes.append(matches[0])

# print(network_map)
print(possible_nodes)


for node in possible_nodes:
    current_node = node
    for count, direction in enumerate(cycle(sequence), start=1):
        current_node = network_map[current_node][direction]
        # print(node, direction, count)

        if current_node[-1] == 'Z':
            ans.append(count)
            break

print(ans)
print(lcm(*ans))
