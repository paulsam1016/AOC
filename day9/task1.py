from itertools import pairwise
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

print(lines)


def next_value(sequence):
    if all(value == 0 for value in sequence):
        return 0
    difference_sequence = [b - a for a, b in pairwise(sequence)]
    return sequence[-1] + next_value(difference_sequence)


print(sum(next_value([int(value) for value in line.split()]) for line in lines))
