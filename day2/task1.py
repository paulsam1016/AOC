import re
from os import path
location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
games = f.readlines()

# ex = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
#
# games = ex.split('\n')

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
    string = game.strip()
    gameId, game = string.split(": ")
    gameSets = game.split('; ')
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
