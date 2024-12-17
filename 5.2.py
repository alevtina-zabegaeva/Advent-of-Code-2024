import functools

def compare(a, b):
    if [a, b] in orders:
        return -1
    elif [b, a] in orders:
        return 1
    else:
        print("!", a, b)
        return 0

def correct(lst, superorder):
    return [value for value in superorder if value in lst]


filename = '5.1input.txt'
# filename = '5.1test.txt'

orders = []
updates = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        orders.append(list(map(int, list(line.strip().split('|')))))
    for line in f:
        updates.append(list(map(int, list(line.strip().split(',')))))

pages = 0
for update in updates:
    corrected = sorted(update, key=functools.cmp_to_key(compare))
    if corrected != update:
        pages += corrected[len(update)//2]

print(pages)
