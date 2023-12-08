import re
from itertools import cycle
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
current_node = 'AAA'
ans = 0

for _input in inputs:
    nodes = re.findall('\w\w\w', _input)
    network_map[nodes[0]] = {'L': nodes[1], 'R': nodes[2]}

# print(network_map)

for count, direction in enumerate(cycle(sequence), start=1):
    current_node = network_map[current_node][direction]
    count += 1

    if current_node == 'ZZZ':
        ans = count
        break

print(ans)
