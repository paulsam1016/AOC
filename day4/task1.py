from os import path

location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

# ex = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
#
# lines = ex.split('\n')

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
