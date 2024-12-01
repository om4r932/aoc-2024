left = []
right = []
distance = 0
# AoC invite : 3490085-ade85e82
# AoC private leaderboard : https://adventofcode.com/2024/leaderboard/private

with open('day1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        x, y = line.split('   ')
        left.append(int(x))
        right.append(int(y))

# Part 1

def isListOfNumbers(l):
    for i in l:
        if not isinstance(i, int):
            return False
    return True


def minIndex(l):
    mini = l[0]
    index = 0
    for i in range(1, len(l)):
        if l[i] < mini:
            mini = l[i]
            index = i
    return index

l = left.copy()
r = right.copy()

while l != [] and r != []:
    min_left = minIndex(l)
    min_right = minIndex(r)

    distance += abs(l[min_left] - r[min_right])
    l.pop(min_left)
    r.pop(min_right)

print(distance)

# Part 2

similarity_score = 0

l = left.copy()
r = right.copy()

for x in l:
    sim_right = r.count(x)
    similarity_score += (sim_right * x)

print(similarity_score)