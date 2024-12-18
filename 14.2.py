import re


filename = '14.1input.txt'
# filename = '14.1test.txt'


xmax, ymax = 101, 103
steps = 10000

positions = []
velocities = []
with open(filename) as f:
    for line in f:
        x, y, v, w = list(map(int, re.findall(r'[-]?\d+', line)))
        positions.append((x, y))
        velocities.append((v, w))

with open("14.2output.txt", "w") as f:
    for j in range(steps):
        new_positions = []
        for i, (x, y) in enumerate(positions):
            new_positions.append(((x + velocities[i][0]) % xmax, (y + velocities[i][1]) % ymax))
        positions = new_positions.copy()
        if j + 1 == 7572: # 53+103*x == 98+101*y x=73, y=74
            for x in range(xmax):
                for y in range(ymax):
                    if (x, y) in positions:
                        print('#', end='', file=f)
                    else:
                        print('.', end='', file=f)
                print(file=f)
            print(j + 1, file=f)
            break

