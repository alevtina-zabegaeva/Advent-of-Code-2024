def change(n):
    if n == 0:
        return [1]
    l = len(str(n))
    if l % 2 == 0:
        return [n // 10**(l // 2), n % 10**(l // 2)]
    return [n * 2024]

filename = '11.1input.txt'
# filename = '11.1test.txt'

with open(filename) as f:
    stones = list(map(int, f.readline().strip().split()))

print(stones)
for _ in range(25):
    next_stones = []
    for stone in stones:
        next_stones.extend(change(stone))
    # print(next_stones)
    stones = next_stones.copy()
print(len(stones))