import re
from os import path
location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
games = f.read().splitlines()

# ex = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
#
# games = ex.split('\n')

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
