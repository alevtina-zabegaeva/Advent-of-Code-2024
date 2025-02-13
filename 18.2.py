filename = '18.1input.txt'
# filename = '18.1test.txt'

with open(filename) as f:
    corrupted_lst = [tuple(map(int, line.strip().split(','))) for line in f]

m = max(corrupted_lst)[0]
n = max(corrupted_lst, key=lambda p: p[1])[1]
# print(m, n)

start = (0, 0)
end = (m, n)

corrupted_start = 1024
blocked = False
corrupted = set(corrupted_lst[:corrupted_start])
for corrupted_i in range(corrupted_start + 1, len(corrupted_lst)):
    current = {start}
    visited = {start}
    i = 0
    corrupted.add(corrupted_lst[corrupted_i])
    while not blocked:
        next_step = set()
        for byte in current:
            for k, l in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x, y = byte[0] + k, byte[1] + l
                if 0 <= x <= m and 0 <= y <= n:
                    if not (x, y) in visited and not (x, y) in corrupted and not (x, y) in current:
                        next_step.add((x, y))
        i += 1
        if (m, n) in next_step:
            break
        if len(next_step) == 0:
            blocked = True
        visited |= next_step
        current = next_step

    if blocked:
        print(corrupted_lst[corrupted_i])
        break
