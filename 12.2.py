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
        garden[x, y] = '.'
        while True:
            nextstep = set()
            for i, j in region:
                for diri, dirj in near:
                    if garden[i + diri, j + dirj] == plot:
                        nextstep.add((i + diri, j + dirj))
                        garden[i + diri, j + dirj] = '.'
            region |= nextstep
            if len(nextstep) == 0:
                break
        regions.append(region)

# print(regions)
price = []
for region in regions:
    perimeter = 0
    for x, y in np.ndindex(garden.shape):
        s = sum(((x, y) in region,
                (x + 1, y) in region,
                (x, y + 1) in region,
                (x + 1, y + 1) in region))
        if s == 1 or s == 3:
            perimeter += 1
        elif s == 2 and ((x, y) in region) == ((x + 1, y + 1) in region):
            perimeter += 2
    price.append(perimeter * len(region))

print(sum(price))
