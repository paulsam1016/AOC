from collections import Counter
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
inputs = list(map(str.split, f.read().splitlines()))

types = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': []}
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ranking = []

# print(inputs)

for hand, bid in inputs:
    counts = Counter(hand)
    match [count for _, count in Counter(hand).most_common()]:
        case 5, *_:
            types['7'].append([hand, bid])
        case 4, *_:
            types['6'].append([hand, bid])
        case 3, 2, *_:
            types['5'].append([hand, bid])
        case 3, *_:
            types['4'].append([hand, bid])
        case 2, 2, *_:
            types['3'].append([hand, bid])
        case 2, *_:
            types['2'].append([hand, bid])
        case _:
            types['1'].append([hand, bid])

# print(types)

for _type in types.values():
    if len(_type) == 1:
        ranking.append(_type[0][1])
        # print(_type[0][1])

    if len(_type) > 1:
        same_rank_order = {hand: bid for hand, bid in _type}
        same_rank_sorted = sorted(same_rank_order.keys(), key=lambda word: [order.index(c) for c in word], reverse=True)
        # print(same_rank_order)
        # print(same_rank_sorted)
        # print([same_rank_order[hand] for hand in same_rank_sorted])
        # print('================================================================')
        ranking.extend([same_rank_order[hand] for hand in same_rank_sorted])

# print(ranking)

total_winnings = 0
for i, bid in enumerate(ranking):
    total_winnings += (i + 1) * int(bid)

print(total_winnings)
