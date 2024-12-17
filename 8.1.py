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
        x3, y3 = x1 - (x2 - x1), y1 - (y2 - y1)
        x4, y4 = x2 + (x2 - x1), y2 + (y2 - y1)
        for x, y in ((x3, y3),  (x4, y4)):
            if check(x, y) and not (x, y) in coords:
                antinodes.add((x, y))

print(len(antinodes))
