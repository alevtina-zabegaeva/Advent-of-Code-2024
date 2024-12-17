import re


filename = '13.1input.txt'
# filename = '13.1test.txt'

limit = 100
priceA, priceB = 3, 1

automats = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        if len(line) != 0:
            automats.append(list(map(int, re.findall(r'\d+', line))))

# print(automats)

tokens = []
for i in range(0, len(automats), 3):
    xa, ya = automats[i]
    xb, yb = automats[i + 1]
    xprize, yprize = automats[i + 2]
    celebrant = xa * yb - xb * ya
    chlorinatora = yb * xprize - xb * yprize
    chlorinatorb = xa * yprize - ya * xprize
    if celebrant != 0 and chlorinatora % celebrant == 0 and chlorinatorb % celebrant == 0:
        na = chlorinatora // celebrant
        nb = chlorinatorb // celebrant
        tokens.append(na * priceA + nb * priceB)
print(sum(tokens))
    
