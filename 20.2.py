import numpy as np


filename = '20.1input.txt'
# filename = '20.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]

input = np.array(input)
m, n = input.shape
maze = np.full((m + 2, n + 2), '#')
maze[1:-1, 1:-1] = input

x, y = np.where(maze == 'S')
x, y = x[0], y[0]
xend, yend = np.where(maze == 'E')
end = (xend[0], yend[0])
maze[*end] = '.'

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

current = [(x, y)]
found = {(x, y): 0}
while len(current) > 0:
    next_steps = [] # [(i, j, score), }
    for curi, curj in current:
        curscore = found[(curi, curj)]
        for diri, dirj in directions:
            next_step = (curi + diri, curj + dirj)
            if maze[*next_step] == '.':
                next_steps.append((*next_step, curscore + 1))
    current = []
    for nexti, nextj, nextscore in next_steps:
        if (nexti, nextj) in found and nextscore < found[(nexti, nextj)] or not (nexti, nextj) in found:
            found[(nexti, nextj)] = nextscore
            current.append((nexti, nextj))
# print(found[*end])

way = [''] * len(found)
for point, score in found.items():
    way[score] = point

max_range = 20
min_diff = 100
# min_diff = 50
difference = 0
d = []
for i, (x, y) in enumerate(way[: - min_diff - 3]):
    for j in range(i + min_diff + 2, len(way)):
        r = abs(x - way[j][0]) + abs(y - way[j][1])
        if r <= max_range and j - i - r >= min_diff:
            difference += 1

print(difference)

