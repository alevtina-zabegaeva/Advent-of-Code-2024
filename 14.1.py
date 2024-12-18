import re
import math


filename = '14.1input.txt'
# filename = '14.1test.txt'


xmax, ymax = 101, 103
# xmax, ymax = 11, 7
steps = 100

positions = []
velocities = []
with open(filename) as f:
    for line in f:
        x, y, v, w = list(map(int, re.findall(r'[-]?\d+', line)))
        positions.append((x, y))
        velocities.append((v, w))

for _ in range(steps):
    new_positions = []
    for i, (x, y) in enumerate(positions):
        new_positions.append(((x + velocities[i][0]) % xmax, (y + velocities[i][1]) % ymax))
    positions = new_positions.copy()
    
quadrants = [0, 0, 0, 0]
xmid, ymid = xmax // 2, ymax // 2
for x, y in positions:
    if x < xmid:
        if y < ymid:
            quadrants[0] += 1
        elif y > ymid:
            quadrants[2] += 1
    elif x > xmid:
        if y < ymid:
            quadrants[1] += 1
        elif y > ymid:
            quadrants[3] += 1
print(math.prod(quadrants))
