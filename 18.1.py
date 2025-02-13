filename = '18.1input.txt'
# filename = '18.1test.txt'

with open(filename) as f:
    corrupted_lst = [tuple(map(int, line.strip().split(','))) for line in f]

print(corrupted_lst)

m = max(corrupted_lst)[0]
n = max(corrupted_lst, key=lambda p: p[1])[1]
print(m, n)

start = (0, 0)
end = (m, n)

current = {start}
visited = {start}
corrupted = set(corrupted_lst[:1024])
i = 0
while True:
    next_step = set()
    # corrupted.add(corrupted_lst[i])
    for byte in current:
        for k, l in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            x, y = byte[0] + k, byte[1] + l
            if 0 <= x <= m and 0 <= y <= n:
                if not (x, y) in visited and not (x, y) in corrupted and not (x, y) in current:
                    next_step.add((x, y))
    # print(next_step)
    i += 1
    if (m, n) in next_step:
        break
    visited |= next_step
    current = next_step

print(i)
