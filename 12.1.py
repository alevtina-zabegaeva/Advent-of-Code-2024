import numpy as np


filename = '12.1input.txt'
# filename = '12.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]
input = np.array(input)
m, n = input.shape
garden = np.full((m + 2, n + 2), '.')
garden[1:-1, 1:-1] = input

near = ((0, 1), (1, 0), (0, -1), (-1, 0))
perimeter_trans = {1: 2, 2: 0, 3: -2, 4: -4}
regions = []
for x, y in np.ndindex(garden.shape):
    plot = garden[x, y]
    if plot != '.':
        region = {(x, y)}
        perimeter = 4
        garden[x, y] = '.'
        while True:
            nextstep = set()
            for i, j in region:
                for diri, dirj in near:
                    if garden[i + diri, j + dirj] == plot:
                        sides = 0
                        for dirk, dirl in near:
                            if (i + diri + dirk, j + dirj + dirl) in region|nextstep:
                                sides += 1
                        perimeter += perimeter_trans[sides]
                        nextstep.add((i + diri, j + dirj))
                        garden[i + diri, j + dirj] = '.'
            region |= nextstep
            if len(nextstep) == 0:
                break
        regions.append((len(region) * perimeter))

print(sum(regions))
