def find_pattern(string):
    rest = set()
    for pattern in patterns:
        l = len(pattern)
        if pattern == string[:l]:
                rest.add(string[l:])
    return rest


filename = '19.1input.txt'
# filename = '19.1test.txt'

designs = []
with open(filename) as f:
    patterns = f.readline().strip().split(", ")
    f.readline()
    for line in f:
        designs.append(line.strip())

possible_counter = 0
for design in designs:
    current_designs = find_pattern(design)
    while len(current_designs) > 0:
        if '' in current_designs:
            possible_counter += 1
            break
        next_designs = set()
        for des in current_designs:
             next_designs |= find_pattern(des)
        current_designs = next_designs
print(possible_counter)