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
    for page1, page2 in orders:
        if page1 in update and page2 in update:
            if update.index(page1) > update.index(page2):
                break
    else:
        pages += update[len(update)//2]

print(pages)
