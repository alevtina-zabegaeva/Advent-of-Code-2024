import numpy as np


filename = '15.1input.txt'
# filename = '15.1test.txt'

warehouse = []
movements = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        warehouse.append([item for item in line.strip() for _ in range(2)])
    for line in f:
        movements.extend(list(line.strip()))

warehouse = np.array(warehouse)
m, n = warehouse.shape
x, y = np.where(warehouse == '@')
x, y = x[0], y[0]

walls = np.where(warehouse == '#')
walls = set(zip(walls[0], walls[1]))
boxes = np.where(warehouse == 'O')
boxes = list(zip(boxes[0], boxes[1]))
left_boxes = boxes[::2]
right_boxes = boxes[1::2]
print(left_boxes)
print(right_boxes)

direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
current = (x, y)
for dir in movements:
    move = direction[dir]
    nextstep = (current[0] + move[0], current[1] + move[1])
    if not nextstep in left_boxes and not nextstep in right_boxes:
        if not nextstep in walls:
            current = nextstep
    elif dir in ('>', '<'):
        moved_boxes_ind = []
        while nextstep in left_boxes or nextstep in right_boxes:
            if dir == '>':
                moved_boxes_ind.append(left_boxes.index(nextstep))
            else:
                moved_boxes_ind.append(right_boxes.index(nextstep))
            nextstep = (nextstep[0], nextstep[1] + move[1] * 2)
        if not nextstep in walls:
            current = (current[0], current[1] + move[1])
            for i in moved_boxes_ind:
                left_boxes[i] = (left_boxes[i][0], left_boxes[i][1] + move[1])
                right_boxes[i] = (right_boxes[i][0], right_boxes[i][1] + move[1])
    else:
        moved_boxes_ind = set()
        current_level = {nextstep}
        wall = False
        if nextstep in left_boxes:
            moved_boxes_ind.add(left_boxes.index(nextstep))
            current_level.add((nextstep[0], nextstep[1] + 1))
        else:
            moved_boxes_ind.add(right_boxes.index(nextstep))
            current_level.add((nextstep[0], nextstep[1] - 1))
        while True:
            next_level = set()
            next_moved_boxes_ind = set()
            for i, j in current_level:
                if (i + move[0], j) in walls:
                    next_moved_boxes_ind = set()
                    next_level = set()
                    wall = True
                    break
                elif (i + move[0], j) in left_boxes:
                    next_moved_boxes_ind.add(left_boxes.index((i + move[0], j)))
                    next_level.add((i + move[0], j))
                    next_level.add((i + move[0], j + 1))
                elif (i + move[0], j) in right_boxes:
                    next_moved_boxes_ind.add(right_boxes.index((i + move[0], j)))
                    next_level.add((i + move[0], j))
                    next_level.add((i + move[0], j - 1))
            if len(next_level) == 0:
                break
            moved_boxes_ind |= next_moved_boxes_ind
            current_level = next_level
        if not wall:
            current = (current[0] + move[0], current[1])
            for i in moved_boxes_ind:
                left_boxes[i] = (left_boxes[i][0] + move[0], left_boxes[i][1])
                right_boxes[i] = (right_boxes[i][0] + move[0], right_boxes[i][1])

for x in range(m):
    for y in range(n):
        if (x, y) in left_boxes:
            print('[', end='')
        elif (x, y) in right_boxes:
            print(']', end='')
        elif (x, y) == current:
            print('@', end='')
        elif (x, y) in walls:
            print('#', end='')
        else:
            print('.', end='')
    print()
print()

GPS_coordinate = [i * 100 + j for i, j in left_boxes]
print(sum(GPS_coordinate))
