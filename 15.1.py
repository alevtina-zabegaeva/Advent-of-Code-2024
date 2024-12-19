import numpy as np


filename = '15.1input.txt'
# filename = '15.1test.txt'

warehouse = []
movements = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        warehouse.append(list(line.strip()))
    for line in f:
        movements.extend(list(line.strip()))

warehouse = np.array(warehouse)
m, n = warehouse.shape
x, y = np.where(warehouse == '@')
x, y = x[0], y[0]
print(warehouse)

walls = np.where(warehouse == '#')
walls = set(zip(walls[0], walls[1]))
boxes = np.where(warehouse == 'O')
boxes = set(zip(boxes[0], boxes[1]))

direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
current = (x, y)
for dir in movements:
    move = direction[dir]
    nextstep = (current[0] + move[0], current[1] + move[1])
    if not nextstep in boxes:
        if not nextstep in walls:
            current = nextstep
    else:
        k = 0
        while nextstep in boxes:
            k += 1
            nextstep = (current[0] + move[0] * k, current[1] + move[1] * k)
        if not nextstep in walls:
            current = (current[0] + move[0], current[1] + move[1])
            boxes.discard(current)
            boxes.add(nextstep)
        # print(boxes)
    
for x in range(m):
    for y in range(n):
        if (x, y) in boxes:
            print('O', end='')
        elif (x, y) == current:
            print('@', end='')
        elif (x, y) in walls:
            print('#', end='')
        else:
            print('.', end='')
    print()
print()

GPS_coordinate = [i * 100 + j for i, j in boxes]
print(sum(GPS_coordinate))
