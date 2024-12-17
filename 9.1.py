filename = '9.1input.txt'
# filename = '9.1test.txt'

with open(filename) as f:
    line = f.readline().strip()
if len(line) % 2 == 1:
    line += '0'

fileid = 0
disk = []
for i in range(0, len(line), 2):
    file = int(line[i])
    disk.extend([fileid]*file)
    fileid += 1
    freespace = int(line[i + 1])
    disk.extend(['.']*freespace)

# print(disk)
i = len(disk) - 1
j = 0
while j < i:
    if disk[i] == '.':
        disk.pop(i)
        i -= 1
    else:
        while j < len(disk) and disk[j] != '.':
            j += 1
        if j < i:
            disk[j] = disk[i]
            disk.pop(i)
            # print(disk)
            i -= 1

checksum = sum(i * n for i, n in enumerate(disk))
print(checksum)
