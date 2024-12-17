filename = '7.1input.txt'
# filename = '7.1test.txt'

results = []
numbers = []
with open(filename) as f:
    for line in f:
        result, *n = line.strip().split()
        results.append(int(result[:-1]))
        numbers.append(list(map(int, n)))

right = []
for i, result in enumerate(results):
    number = numbers[i]
    res = [[number[0]]]
    for j in range(1, len(number)):
        res.append([])
        for r in res[j - 1]:
            for new in (r + number[j], r * number[j], int(str(r) + str(number[j]))):
                if new <= result:
                    res[j].append(new)
        if len(res[j]) == 0:
            break
    else:
        if result in res[-1]:
            right.append(result)

print(sum(right))
