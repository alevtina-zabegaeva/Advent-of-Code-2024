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
found = {(x, y, 0): (0, {(x, y)})}
while len(current) > 0:
    nextsteps = [] # [((i, j, dir), (score, {(ii, jj), (kk, ll), ...}))]
    for curi, curj, curd in current:
        curscore, curway = found[(curi, curj, curd)]
        diri, dirj = directions[curd]
        next_forward = (curi + diri, curj + dirj)
        if maze[*next_forward] == '.':
            nextsteps.append(((*next_forward, curd), (curscore + 1, curway|{next_forward})))
        for k in (-1, 1):
            nextd = (curd + k) % 4
            nextdiri, nextdirj = directions[nextd]
            next_side = (curi + nextdiri, curj + nextdirj)
            if maze[*next_side] == '.':
                nextsteps.append(((*next_side, nextd), (curscore + 1001, curway|{next_side})))
    current = []
    for (nexti, nextj, nextd), (nextscore, nextway) in nextsteps:
        if (nexti, nextj, nextd) in found:
            if nextscore < found[(nexti, nextj, nextd)][0]:
                found[(nexti, nextj, nextd)] = (nextscore, nextway)
                current.append((nexti, nextj, nextd))
            elif nextscore == found[(nexti, nextj, nextd)][0]:
                found[(nexti, nextj, nextd)] = (nextscore, nextway|found[(nexti, nextj, nextd)][1])
        else:
            found[(nexti, nextj, nextd)] = (nextscore, nextway)
            current.append((nexti, nextj, nextd))

ways = []
for k in range(4):
    if (*end, k) in found:
        ways.append(found[(*end, k)])
way = min(ways, key=lambda w: w[0])
print(len(way[1]))
