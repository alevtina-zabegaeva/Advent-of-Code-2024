filename = '17.1input.txt'
# filename = '17.1test.txt'

registers = []
program = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        registers.append(int(line.split()[-1]))
    for line in f:
        program = list(map(int, line.split()[-1].split(',')))

a, b, c = registers

output = []
i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i + 1]
    literal_operand = operand
    combo_operand = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c, 7: 1}[operand]
    if opcode == 0:
        a = int(a / 2**combo_operand)
    elif opcode == 1:
        b = b ^ literal_operand
    elif opcode == 2:
        b = combo_operand % 8
    elif opcode == 3:
        if a != 0:
            i = literal_operand - 2
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        output.append(str(combo_operand % 8))
    elif opcode == 6:
        b = int(a / 2**combo_operand)
    elif opcode == 7:
        c = int(a / 2**combo_operand)
    i += 2

print(','.join(output))
    