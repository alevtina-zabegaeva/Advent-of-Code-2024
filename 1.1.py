filename = '1.1input.txt'
# filename = '1.1test.txt'

list1 = []
list2 = []
with open(filename) as f:
    for line in f:
        number1, number2 = map(int, line.split())
        list1.append(number1)
        list2.append(number2)
list1.sort()
list2.sort()
res = sum(abs(list1[i] - list2[i])for i in range(len(list1)))
print(res)
