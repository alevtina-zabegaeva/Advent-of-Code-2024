from collections import Counter

filename = '1.1input.txt'
# filename = '1.1test.txt'

list1 = []
list2 = []
with open(filename) as f:
    for line in f:
        number1, number2 = map(int, line.split())
        list1.append(number1)
        list2.append(number2)
list2 = Counter(list2)
similarity = sum(number1 * list2[number1] for number1 in list1)
print(similarity)
