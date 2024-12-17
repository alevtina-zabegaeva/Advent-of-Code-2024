import numpy as np


def rotate(a, b):
    return (b, -a)


filename = '6.1input.txt'
# filename = '6.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]
input = np.array(input)
m, n = input.shape
i, j = np.where(input == '^')
i, j = i[0], j[0]
obstructions = np.where(input == '#')
obstructions = set(zip(obstructions[0], obstructions[1]))

current = (i, j)
way = set()
direction = (-1, 0)
while True:
    next_position = (current[0] + direction[0], current[1] + direction[1])
    if next_position[0] < 0 or next_position[1] < 0 or next_position[0] >= m or next_position[1] >= n:
        break
    if next_position in obstructions:
         direction = rotate(*direction)
    else:
        current = next_position
        way.add(current)
way.discard((i, j))

counter = 0
for k, l in way:
    current = (i, j)
    direction = (-1, 0)
    visited = {(*current, *direction)}
    while True:
        next_position = (current[0] + direction[0], current[1] + direction[1])
        if next_position[0] < 0 or next_position[1] < 0 or next_position[0] >= m or next_position[1] >= n:
            break
        if next_position in obstructions or next_position == (k, l):
            direction = rotate(*direction)
        else:
            current = next_position
            current_dir = (*current, *direction)
            if current_dir in visited:
                counter += 1
                break
            visited.add(current_dir)

print(counter)
