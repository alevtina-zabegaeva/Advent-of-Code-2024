def evolve(num):
    num = (num * 64 ^ num) % 16777216
    num = (num // 32 ^ num) % 16777216
    num = (num * 2048 ^ num) % 16777216
    return num


filename = '22.1input.txt'
# filename = '22.1test.txt'

with open(filename) as f:
    secret_numbers = [int(line.strip()) for line in f]

n = 2000
s = 0
for secret_number in secret_numbers:
    for _ in range(n):
        secret_number = evolve(secret_number)
    s += secret_number
print(s)
