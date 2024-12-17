import numpy as np

def check(frame, i, j):
    directions = ( 
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1),           (0, 1), 
        (1, -1),  (1, 0),  (1, 1) 
    )
    count = 0
    for d in directions:
        if frame[i + d[0], j + d[1]] == 'M' and frame[i + d[0] * 2, j + d[1] * 2] == 'A' and frame[i + d[0] * 3, j + d[1] * 3] == 'S':
            count += 1
    return count

filename = '4.1input.txt'
# filename = '4.1test.txt'

with open(filename) as f:
    lists = [list(line.strip()) for line in f]

lists = np.array(lists)
m, n = lists.shape
frame = np.full((m + 6, n + 6), '.')
frame[3:-3, 3:-3] = lists

xmas = 0
for i in range(3, 3 + m):
    for j in range(3, 3 + n):
        if frame[i, j] == 'X':
            xmas += check(frame, i, j)
   
print(xmas)
