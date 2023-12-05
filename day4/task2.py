from collections import defaultdict
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

winCounts = defaultdict(lambda: 0, {})

for line in lines:
    card, string = line.split(': ')
    card = int(card.split()[1])
    winners, numbers = map(str.split, string.split(' | '))
    # print(card)
    # print(winners)
    # print(numbers)
    matches = sum(x in winners for x in numbers)
    winCounts[card] += 1
    for i in range(card + 1, card + matches + 1):
        winCounts[i] += winCounts[card]
    # print(matches)
    # print(winCount)

# print(winCount)
print(f'total scratchcards: {sum(winCounts.values())}')
