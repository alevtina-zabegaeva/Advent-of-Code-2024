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
while i >= 0:
    if disk[i] == '.':
        i -= 1
    else:
        length = 1
        while disk[i - length] == disk[i]:
            length += 1
        j = 0
        while j < i - length:
            if disk[j:j + length] == ['.'] * length:
                disk[j:j + length] = [disk[i]] * length
                disk[i - length + 1:i + 1] = ['.'] * length
                print(i)
                break
            j += 1
        i -= length

# print(disk)
checksum = sum(i * n for i, n in enumerate(disk) if n != '.')
print(checksum)
