import re
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

sum_cali = 0

for line in lines:
    first = re.search("\d", line)  # Find first digit
    reversedLine = line[::-1]  # Reverse String
    last = re.search("\d", reversedLine)  # Find last digit
    number = int(first[0] + last[0])

    sum_cali += number

print(sum_cali)
