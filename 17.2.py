def bin3(n):
    return ('00' + str(bin(n)))[-3:]


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

a_lst = ['0o']
for p in program[::-1]:
    a_lst_next = []
    for a_cur in a_lst:
        for i in range(8):
            ai_cur = int(a_cur + str(i), 0)
            b = ((ai_cur >> 3) << 3) ^ ai_cur
            b = b ^ 3
            c = ai_cur >> b
            b = b ^ 4
            b = b ^ c
            out = ((b >> 3) << 3) ^ b
            if out == p:
                a_lst_next.append(oct(ai_cur))
    a_lst = a_lst_next.copy()

# print(a_lst)

a, b, c = registers
for a8 in a_lst:
    a = int(a8, 0)
    output = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        literal_operand = operand
        combo_operand = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c, 7: 1}[operand]
        if opcode == 0:
            a = a >> combo_operand
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
            output.append(combo_operand % 8)
            l = len(output)
            if output[-1] != program[l - 1]:
                break
        elif opcode == 6:
            b = a >> combo_operand
        elif opcode == 7:
            c = a >> combo_operand
        i += 2
    if output == program:
        print(a8, output, program)
        break

print(int(a8, 0))
   