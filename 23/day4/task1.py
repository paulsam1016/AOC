from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

totalPoints = 0

for line in lines:
    string = line.split(': ')[1]
    winners, numbers = map(str.split, string.split(' | '))
    # print(winners)
    # print(numbers)
    matches = sum(x in numbers for x in winners)
    if matches > 0:
        totalPoints += 2 ** (int(matches) - 1)
    # print(matches)
    # print(points)

print(f'totalPoints : {totalPoints}')
