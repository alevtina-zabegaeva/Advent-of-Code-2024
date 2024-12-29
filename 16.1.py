import numpy as np


filename = '16.1input.txt'
# filename = '16.1test.txt'

with open(filename) as f:
    maze = [list(line.strip()) for line in f]

maze = np.array(maze)
m, n = maze.shape
x, y = np.where(maze == 'S')
x, y = x[0], y[0]
xend, yend = np.where(maze == 'E')
end = (xend[0], yend[0])
maze[*end] = '.'
score = 1000

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
current = [(x, y, 0)]
found = {(x, y, 0): 0}
while len(current) > 0:
    nextsteps = {}
    for curi, curj, curd in current:
        curscore = found[(curi, curj, curd)]
        diri, dirj = directions[curd]
        next_forward = (curi + diri, curj + dirj)
        if maze[*next_forward] == '.':
            if (*next_forward, curd) in nextsteps:
                nextsteps[(*next_forward, curd)] = min(curscore + 1, nextsteps[(*next_forward, curd)])
            else:
                nextsteps[(*next_forward, curd)] = curscore + 1
        for k in (-1, 1):
            nextd = (curd + k) % 4
            nextdiri, nextdirj = directions[nextd]
            next_side = (curi + nextdiri, curj + nextdirj)
            if maze[*next_side] == '.':
                if (*next_side, nextd) in nextsteps:
                    nextsteps[(*next_side, nextd)] = min(curscore + 1001, nextsteps[(*next_side, nextd)])
                else:
                    nextsteps[(*next_side, nextd)] = curscore + 1001
    current = []
    for (nexti, nextj, nextd), nextscore in nextsteps.items():
        if (nexti, nextj, nextd) in found and nextscore < found[(nexti, nextj, nextd)] or not (nexti, nextj, nextd) in found:
            found[(nexti, nextj, nextd)] = nextscore
            current.append((nexti, nextj, nextd))

# for x in range(m):
#     for y in range(n):
#         print(maze[x, y], end='')
#     print()
# print()

ways = []
for k in range(4):
    if (*end, k) in found:
        ways.append(found[(*end, k)])
print(min(ways))
