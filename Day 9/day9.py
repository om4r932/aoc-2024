disk = []
import sys

with open('day9_test.txt') as f:
    for line in f:
        disk += [int(x) for x in line.strip()]

cursor = 0
separator = "."

actual = cursor

diskmap = []
for data in disk:
    for _ in range(data):
        diskmap.append(actual)
    if isinstance(actual, str):
        cursor += 1
        actual = cursor
    else:
        actual = "."

def checkLinearity(liste):
    changeCount = 0
    actualType = type(liste[0])
    for x in range(1, len(liste)):
        if isinstance(liste[x], actualType):
            continue
        else:
            changeCount += 1
            actualType = type(liste[x])
    return changeCount < 2

# Part 1
def part1():
    for x in range(len(diskmap)):
        sys.stdout.write(f"\r{x}/{len(diskmap)}")
        if diskmap[x] == ".":
            i = len(diskmap) - 1
            while i != 0:
                if diskmap[i] == ".":
                    i -= 1
                else:
                    break
            if i == 0:
                continue
            diskmap[x], diskmap[i] = diskmap[i], diskmap[x]
            if checkLinearity(diskmap):
                break
        sys.stdout.flush()

    total = 0
    for x in range(len(diskmap)):
        if isinstance(diskmap[x], int):
            total += x * diskmap[x]
    return total

# Part 2

def part2():
    def getDotIntervals():
        x = 0
        dotIntervals = []
        while x < len(diskmap):
            if diskmap[x] == '.':
                dotLength = 0
                i = x
                while diskmap[i] == '.':
                    dotLength += 1
                    i += 1
                    if i > len(diskmap) - 1:
                        break
                dotInterval = (x, x + dotLength - 1)
                dotIntervals.append(dotInterval)
                x = x + dotLength - 1
            x += 1
        return dotIntervals
    
    def getNumberRanges():
        numberRanges = []
        x = len(diskmap) - 1
        while x >= 0:
            if diskmap[x] != '.' and diskmap[x] != 0:
                numberRanges.append((x - diskmap.count(diskmap[x]) + 1, x + 1))
                x = x - diskmap.count(diskmap[x]) + 1
            x -= 1
        return numberRanges

    
part2()