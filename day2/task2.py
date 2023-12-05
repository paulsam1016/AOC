import re
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
games = f.read().splitlines()

sumPowers = 0


def find_cubes(game_set, color):
    cubes = re.findall(f'\d* {color}', game_set)
    if cubes:
        return int(cubes[0].split(' ')[0])
    else:
        return 0


for game in games:
    redPower = 1
    greenPower = 1
    bluePower = 1
    gameId, gameSets = game.split(": ")
    gameSets = gameSets.split('; ')
    for gameSet in gameSets:
        # 1
        # Get number of cubes per color
        red = find_cubes(gameSet, 'red')
        green = find_cubes(gameSet, 'green')
        blue = find_cubes(gameSet, 'blue')
        # find the fewest number of cubes per color
        redPower = max(red, redPower)
        greenPower = max(green, greenPower)
        bluePower = max(blue, bluePower)

        # 2
        # Better way for Python
        # colors = [x.split() for x in gameSet.split(", ")]
        # counts = {b: int(a) for a, b in colors}
        # redPower = max(redPower, counts.get("red", 0))
        # greenPower = max(greenPower, counts.get("green", 0))
        # bluePower = max(bluePower, counts.get("blue", 0))

    sumPowers += redPower * greenPower * bluePower

print(f'sumPowers: {sumPowers}')
