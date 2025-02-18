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

print(found[*end])

# for x in range(m + 2):
#     for y in range(n + 2):
#         if (x, y) in found:
#             print(f"{found[x, y]:02d}", end='')
#         else:
#             print(maze[x, y], end=' ')
#     print()
# print()

difference = 0
for (x, y), score in found.items():
    for dirx, diry in ((0, 2), (2, 0)):
        point = (x + dirx, y + diry)
        if point in found:
            if (diff := abs(found[point] - score) - 2) >= 100:
                difference += 1

print(difference)
