from collections import Counter


def find_pattern(string):
    rest = Counter()
    for pattern in patterns:
        l = len(pattern)
        if pattern == string[:l]:
                rest[string[l:]] += 1
    return rest


filename = '19.1input.txt'
# filename = '19.1test.txt'

designs = []
with open(filename) as f:
    patterns = f.readline().strip().split(", ")
    f.readline()
    for line in f:
        designs.append(line.strip())

possible_counters = []
for design in designs:
    possible_counters.append(0)
    current_designs = find_pattern(design)
    while len(current_designs) > 0:
        next_designs = Counter()
        for des in current_designs:
            if des == '':
                possible_counters[-1] += current_designs[des]
            else:
                new = find_pattern(des)
                for n in new:
                    next_designs[n] += current_designs[des] * new[n]
        current_designs = next_designs

print(sum(possible_counters))
