import numpy as np

def check(frame, i, j):
    if ((frame[i + 1, j + 1] == 'M' and frame[i - 1, j - 1] == 'S' or
        frame[i + 1, j + 1] == 'S' and frame[i - 1, j - 1] == 'M') and
        (frame[i + 1, j - 1] == 'M' and frame[i - 1, j + 1] == 'S' or
        frame[i + 1, j - 1] == 'S' and frame[i - 1, j + 1] == 'M')):
        return 1
    return 0

filename = '4.1input.txt'
# filename = '4.1test.txt'

with open(filename) as f:
    lists = [list(line.strip()) for line in f]

lists = np.array(lists)
m, n = lists.shape
frame = np.full((m + 2, n + 2), '.')
frame[1:-1, 1:-1] = lists

xmas = 0
for i in range(1, 1 + m):
    for j in range(1, 1 + n):
        if frame[i, j] == 'A':
            xmas += check(frame, i, j)
   
print(xmas)
