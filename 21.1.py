from copy import deepcopy


filename = '21.1input.txt'
# filename = '21.1test.txt'

with open(filename) as f:
    codes = [list(line.strip()) for line in f]

print(codes)

numeric_keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
                  '4': (1, 0), '5': (1, 1), '6': (1, 2),
                  '1': (2, 0), '2': (2, 1), '3': (2, 2),
                               '0': (3, 1), 'A': (3, 2)}
keypad = {              '^': (0, 1), 'A': (0, 2),
           '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

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

n = 2
codes_prev = deepcopy(codes2)
for i in range(n):
    codesn = []
    for code in codes_prev:
        codesn.append([])
        coord_x, coord_y = keypad['A']
        for symbol in code:
            coord_next_x, coord_next_y = keypad[symbol]
            delta_x, delta_y = coord_next_x - coord_x, coord_next_y - coord_y
            if coord_next_x == 0 and coord_y == 0:
                codesn[-1].extend(['>'] * delta_y)
                codesn[-1].extend(['^'] * (-delta_x))
            elif coord_next_y == 0 and coord_x == 0:
                codesn[-1].extend(['v'] * delta_x)
                codesn[-1].extend(['<'] * (-delta_y))
            else:
                if delta_y < 0:
                    codesn[-1].extend(['<'] * (-delta_y))
                if delta_x > 0:
                    codesn[-1].extend(['v'] * delta_x)
                elif delta_x < 0:
                    codesn[-1].extend(['^'] * (-delta_x))
                if delta_y > 0:
                    codesn[-1].extend(['>'] * delta_y)
            codesn[-1].append('A')
            coord_x, coord_y = coord_next_x, coord_next_y
    codes_prev = deepcopy(codesn)

s = sum(len(code) * int(''.join(codes[i][:-1])) for i, code in enumerate(codesn))
print(s)
