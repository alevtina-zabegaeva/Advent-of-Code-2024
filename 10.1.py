import numpy as np


filename = '10.1input.txt'
# filename = '10.1test.txt'

with open(filename) as f:
    input = [list(map(int, line.strip())) for line in f]
input = np.array(input)

m, n = input.shape
frame = np.full((m + 2, n + 2), -1)
frame[1:-1, 1:-1] = input
trailheads = np.where(frame == 0)
trailheads = dict.fromkeys(zip(trailheads[0], trailheads[1]), 0)

# print(frame)
# print(trailheads)

near = ((0, 1), (1, 0), (0, -1), (-1, 0))
for x, y in trailheads:
    step = {(x, y)}
    for h in range(1, 10):
        nextstep = set()
        for i, j in step:
            for diri, dirj in near:
                if frame[i + diri, j + dirj] == h:
                    nextstep.add((i + diri, j + dirj))
        step = nextstep
    trailheads[(x, y)] = len(step)

print(trailheads)
print(sum(trailheads.values()))
