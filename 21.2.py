from copy import deepcopy
from collections import Counter


def str_to_pairs(l):
    l = 'A' + l
    p = Counter()
    for i in range(len(l) - 1):
        p.update([l[i:i + 2]])
    return p

def pairs_next(p):
    next_pairs = Counter()
    for pair, value in p.items():
        next_line = str_to_pairs(ways[pair])
        for k in next_line.keys():
            next_line[k] = next_line[k] * value
        next_pairs.update(next_line)
    return next_pairs

filename = '21.1input.txt'
# filename = '21.1test.txt'

with open(filename) as f:
    codes = [list(line.strip()) for line in f]

numeric_keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
                  '4': (1, 0), '5': (1, 1), '6': (1, 2),
                  '1': (2, 0), '2': (2, 1), '3': (2, 2),
                               '0': (3, 1), 'A': (3, 2)}
keypad = {              '^': (0, 1), 'A': (0, 2),
           '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

ways = {'^^': 'A', '^A': '>A', '^<': 'v<A', '^v': 'vA', '^>': 'v>A',
        'A^': '<A', 'AA': 'A', 'A<': 'v<<A', 'Av': '<vA', 'A>': 'vA',
        '<^': '>^A', '<A': '>>^A', '<<': 'A', '<v': '>A', '<>': '>>A',
        'v^': '^A', 'vA': '^>A', 'v<': '<A', 'vv': 'A', 'v>': '>A',
        '>^': '<^A', '>A': '^A', '><': '<<A', '>v': '<A', '>>': 'A'}
pairs_cnt = Counter({'^^': 0, '^A': 0, '^<': 0, '^v': 0, '^>': 0,
                     'A^': 0, 'AA': 0, 'A<': 0, 'Av': 0, 'A>': 0,
                     '<^': 0, '<A': 0, '<<': 0, '<v': 0, '<>': 0,
                     'v^': 0, 'vA': 0, 'v<': 0, 'vv': 0, 'v>': 0,
                     '>^': 0, '>A': 0, '><': 0, '>v': 0, '>>': 0})

codes2 = []
for code in codes:
    codes2.append([])
    coord_x, coord_y = numeric_keypad['A']
    for symbol in code:
        coord_next_x, coord_next_y = numeric_keypad[symbol]
        delta_x, delta_y = coord_next_x - coord_x, coord_next_y - coord_y
        if coord_next_x == 3 and coord_y == 0:
            codes2[-1].extend(['>'] * delta_y)
            codes2[-1].extend(['v'] * delta_x)
        elif coord_next_y == 0 and coord_x == 3:
            codes2[-1].extend(['^'] * (-delta_x))
            codes2[-1].extend(['<'] * (-delta_y))
        else:
            if delta_y < 0:
                codes2[-1].extend(['<'] * (-delta_y))
            if delta_x > 0:
                codes2[-1].extend(['v'] * delta_x)
            elif delta_x < 0:
                codes2[-1].extend(['^'] * (-delta_x))
            if delta_y > 0:
                codes2[-1].extend(['>'] * delta_y)
        codes2[-1].append('A')
        coord_x, coord_y = coord_next_x, coord_next_y

codes_pairs = [str_to_pairs(''.join(code)) for code in codes2]
n = 25
codes_prev = deepcopy(codes_pairs)
for i in range(n):
    codes_pairs = [pairs_next(code_pairs) for code_pairs in codes_prev]
    codes_prev = deepcopy(codes_pairs)

s = sum(sum(code_pairs.values()) * int(''.join(codes[i][:-1])) for i, code_pairs in enumerate(codes_pairs))
print(s)
