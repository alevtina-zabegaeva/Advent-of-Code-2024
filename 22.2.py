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
sequences_all = []
sequenses_sum = set()
for secret_number in secret_numbers:
    price = secret_number % 10
    differences = []
    for _ in range(3):
        secret_number = evolve(secret_number)
        next_price = secret_number % 10
        differences.append(price - next_price)
        price = next_price
    sequences_all.append({})
    for _ in range(n - 3):
        secret_number = evolve(secret_number)
        next_price = secret_number % 10
        differences.append(price - next_price)
        price = next_price
        diff = tuple(differences)
        sequenses_sum.add(diff)
        differences.pop(0)
        if not diff in sequences_all[-1]:
            sequences_all[-1][diff] = price

max_price = 0
for sequence_sell in sequenses_sum:
    price = 0
    for sequence_all in sequences_all:
        if sequence_sell in sequence_all:
            price += sequence_all[sequence_sell]
    max_price = max(price, max_price)

print(max_price)
