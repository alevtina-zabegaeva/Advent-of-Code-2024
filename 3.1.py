import re

filename = '3.1input.txt'
# filename = '3.1test.txt'

with open(filename) as f:
    program = [line.strip() for line in f]

muls = []
for line in program:
    muls.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)', line))
res = 0
for mul in muls:
    m = list(map(int, mul[4:-1].split(',')))
    res += m[0] * m[1]
    
print(res)
