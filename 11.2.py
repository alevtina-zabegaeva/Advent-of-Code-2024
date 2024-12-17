from collections import Counter


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
    stones = Counter(map(int, f.readline().strip().split()))

print(stones)
for i in range(75):
    next_stones = Counter()
    for stone, value in stones.items():
        for new_stone in change(stone):
            next_stones[new_stone] += value
    stones = next_stones.copy()
    print(i + 1, len(stones))
print(sum(stones.values()))
