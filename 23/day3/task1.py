import re
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

sumPartNumbers = 0

for row, line in enumerate(lines):
    matches = re.finditer(r'\d+', line)

    for match in matches:
        partNumber = int(match.group(0))
        # print(f'match:          {match}')
        # print(f'number:         {partNumber}')

        # print(f'match start:    {start}')
        # print(f'match end :     {end}')

        for r in [row - 1, row, row + 1]:
            if -1 < r < len(lines):
                searchLine = lines[r].rstrip()
                for c in range(match.start() - 1, match.end() + 1):
                    if -1 < c < len(searchLine) and not searchLine[c].isnumeric() and searchLine[c] != '.':
                        sumPartNumbers += partNumber
                        # print('||||||||IS PART||||||||')
                        break
        # print('------------------------')

print(f'sum : {sumPartNumbers}')
