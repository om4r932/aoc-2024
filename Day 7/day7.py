import itertools
values = []

with open('day7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        v = line.strip().split(': ')
        values.append((int(v[0]), [int(val) for val in v[1].split(' ')]))
# operations = ['+', '*'] # For part 1
operations = ['+', '*', '||'] # For part 2

def calibrate(values):
    c = 0
    for target, valueList in values:
        working = False
        for comb in itertools.product(operations, repeat=len(valueList)-1):
            result = valueList[0]
            for i in range(1, len(valueList)):
                if comb[i-1] == '+':
                    result += valueList[i]
                elif comb[i-1] == '||':
                    result = int(str(result) + str(valueList[i]))
                else:
                    result *= valueList[i]
            if result == target:
                working = True
        if working:
            c += target
    return c

print(calibrate(values))