from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
    LL = 7
    UL = 27
else:
    f = open(file=f"{location}/input.txt")
    LL = 200000000000000
    UL = 400000000000000
lines = f.read().splitlines()

total_intersection = 0

for i, line1 in enumerate(lines):
    for line2 in lines[:i]:
        pos1, v1 = [tuple(map(int, x.split(', '))) for x in line1.split(' @ ')]
        pos2, v2 = [tuple(map(int, x.split(', '))) for x in line2.split(' @ ')]
        a1 = v1[1]
        b1 = -v1[0]
        c1 = v1[1] * pos1[0] - v1[0] * pos1[1]
        a2 = v2[1]
        b2 = -v2[0]
        c2 = v2[1] * pos2[0] - v2[0] * pos2[1]

        if v1[1] * -v2[0] == v2[1] * -v1[0]:
            continue
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if LL <= x <= UL and LL <= y <= UL:
            if all((x - hail[0][0]) * hail[1][0] >= 0 and (y - hail[0][1]) * hail[1][1] >= 0 for hail in ((pos1, v1), (pos2, v2))):
                total_intersection += 1

print(total_intersection)
