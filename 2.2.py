filename = '2.1input.txt'
# filename = '2.1test.txt'

def safe(lst):
    diff = lst[1] - lst[0]
    if diff > 0:
        inc = 1
    elif diff < 0:
        inc = -1
    else:
        return False
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        if diff * inc <= 0 or abs(diff) > 3:
            return False
    return True

def safe_dampener(lst):
    if safe(lst):
        return True
    for i in range(len(lst)):
        if safe(lst[:i] + lst[i + 1:]):
            return True
    return False


with open(filename) as f:
    reports = [list(map(int, line.split())) for line in f]
safe_count = sum(safe_dampener(report) for report in reports)
print(safe_count)
