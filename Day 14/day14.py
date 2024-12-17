import os, sys, time

robotStats = {}

mapDimWide, mapDimTall = 101, 103
mapRobots = [[[] for i in range(mapDimWide)] for j in range(mapDimTall)]

with open('day14.txt', 'r', encoding='utf-8') as f:
    i = 1
    for line in f:
        robot = {}
        l = line.strip().split(" ")
        speed = l[1].replace("v=", "")
        robot["speed"] = tuple(map(int, speed.split(",")))
        initPos = l[0].replace('p=', '')
        robot['initPos'] = tuple(map(int, initPos.split(",")))
        robot['currPos'] = robot['initPos']
        robotStats[i] = robot
        i += 1

# speed = (x, y), x > 0 = right, y > 0 = down

def printMap(mapRobots):
    for x in mapRobots:
        for y in x:
            print(y, end=" ")
        print()
    print('\n')

for i, robot in robotStats.items():
    x, y = robot['currPos']
    mapRobots[y][x].append(i)

seconds = 1
maxSeconds = 1000000
while seconds != maxSeconds + 1:
    newMap = [[[] for i in range(mapDimWide)] for j in range(mapDimTall)]
    for i, robot in robotStats.items():
        x, y = robot['currPos']
        mapRobots[y][x].remove(i)
        x, y = robot['currPos']
        x = (x + robot['speed'][0]) % mapDimWide
        y = (y + robot['speed'][1]) % mapDimTall
        robot['currPos'] = (x, y)
        mapRobots[y][x].append(i)
        newMap[y][x].append(i)

    for a in range(mapDimTall):
        for b in range(mapDimWide):
            if len(newMap[a][b]) > 0:
                newMap[a][b] = len(newMap[a][b])
            else:
                newMap[a][b] = '.'

    
    if "111111111" in "".join([str(newMap[i][j]) for j in range(mapDimWide) for i in range(mapDimTall)]): # Part 2
        sys.stdout.flush()
        print("Finished", seconds)
        break

    sys.stdout.write(f"\r{seconds}")
    sys.stdout.flush()
    seconds += 1


# Part 1
# Separate the map into 4 quadrants (get rid of the robots in the middle too)

# quadrant1 = [[mapRobots[i][j] for j in range(mapDimWide // 2)] for i in range(mapDimTall // 2)]
# quadrant2 = [[mapRobots[i][j] for j in range(mapDimWide // 2 + 1, mapDimWide)] for i in range(mapDimTall // 2)]
# quadrant3 = [[mapRobots[i][j] for j in range(mapDimWide // 2)] for i in range(mapDimTall // 2 + 1, mapDimTall)]
# quadrant4 = [[mapRobots[i][j] for j in range(mapDimWide // 2 + 1, mapDimWide)] for i in range(mapDimTall // 2 + 1, mapDimTall)]

# def lenQuadrant(quadrant):
#     count = 0
#     for x in quadrant:
#         for y in x:
#             if isinstance(y, int):
#                 count += y
#     return count

# print(lenQuadrant(quadrant1) * lenQuadrant(quadrant2) * lenQuadrant(quadrant3) * lenQuadrant(quadrant4))