import re
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
games = f.read().splitlines()

redLimit = 12
greenLimit = 13
blueLimit = 14
sumIds = 0


def find_cubes(game_set, color):
    cubes = re.findall(f'\d* {color}', game_set)
    if cubes:
        return int(cubes[0].split(' ')[0])
    else:
        return 0


for game in games:
    gameId, gameSets = game.split(": ")
    gameSets = gameSets.split('; ')
    for gameSet in gameSets:
        # 1
        # Get number of cubes per color
        red = find_cubes(gameSet, 'red')
        green = find_cubes(gameSet, 'green')
        blue = find_cubes(gameSet, 'blue')
        if red > redLimit or green > greenLimit or blue > blueLimit:
            break

        # 2
        # Better way for Python
        # colors = [x.split() for x in gameSet.split(", ")]
        # counts = {b: int(a) for a, b in colors}
        # if counts.get("red", 0) > redLimit or counts.get("green", 0) > greenLimit or counts.get("blue", 0) > blueLimit:
        #     break
    else:
        sumIds += int(gameId.split()[-1])

print(f'sumIds: {sumIds}')
