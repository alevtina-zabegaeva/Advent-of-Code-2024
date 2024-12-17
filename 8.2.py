import numpy as np
from collections import defaultdict
from itertools import combinations


def check(a, b):
    if a >= 0 and a < m and b >=0 and b < n:
        return True
    return False


filename = '8.1input.txt'
# filename = '8.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]
input = np.array(input)
m, n = input.shape

antenns = defaultdict(list)
for (x, y), value in np.ndenumerate(input):
    if value != '.':
        antenns[value].append((x, y))

antinodes = set()
for antenn, coords in antenns.items():
    for (x1, y1), (x2, y2) in combinations(coords, 2):
        antinodes.add((x1, y1))
        antinodes.add((x2, y2))
        i = 1
        while True:
            x, y = x1 - i*(x2 - x1), y1 - i*(y2 - y1)
            if not check(x, y):
                break
            if not (x, y) in coords:
                antinodes.add((x, y))
            i += 1
        i = 1
        while True:
            x, y = x2 + i*(x2 - x1), y2 + i*(y2 - y1)
            if not check(x, y):
                break
            if not (x, y) in coords:
                antinodes.add((x, y))
            i += 1

print(len(antinodes))
