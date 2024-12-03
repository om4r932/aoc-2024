import re # Bibliothèque regex

lines = []

with open('day3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        r = line.strip()
        lines.append(r)

# Part 1
def getMul(text): # Recherche les textes du style "mul(x, y)"
    return re.findall(r'mul\(\d+,\d+\)', text)

allMuls = []

for line in lines:
    allMuls += getMul(line)

def getMulVal(text):
    nums = re.findall(r'\d+', text)
    return int(nums[0]) * int(nums[1])

mulVals = [getMulVal(mul) for mul in allMuls] # Multiple les nombres trouvés
print(sum(mulVals))

# Part 2

def getMulAndFunctions(text): # Dans ce cas, mul(x, y), do() ou don't()
    return re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', text)

allMulsAndFunctions = []

for line in lines:
    allMulsAndFunctions += getMulAndFunctions(line)

do = True
mulsDos = 0
for mulOrMode in allMulsAndFunctions:
    if 'do()' == mulOrMode:
        do = True
    elif "don't()" == mulOrMode:
        do = False
    elif 'mul' in mulOrMode and do:
        mulVal = getMulVal(mulOrMode)
        mulsDos += mulVal
    else:
        continue

print(mulsDos)