from termcolor import colored

trailheads = []
with open('day10_test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        l = []
        for c in line.strip():
            if c.isnumeric():
                l.append(int(c))
            else:
                l.append(c)
        trailheads.append(l)

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def getDelta(trailheads, pos, val):
    deltaValPos = set()
    for dx, dy in deltas:
        x, y = pos
        x += dx
        y += dy
        if 0 <= x < len(trailheads) and 0 <= y < len(trailheads[0]) and trailheads[x][y] == val:
            deltaValPos.add((x, y))
    return deltaValPos

def makeGraph(trailheads, start=0):
    graphs = []
    for i in range(len(trailheads)):
        for j in range(len(trailheads[0])):
            if trailheads[i][j] == start:
                graph = {}
                for val in range(10):
                    graph[val] = getDelta(trailheads, (i, j), val)
                graphs.append(graph)
    return graphs

graphs = []
for start in range(10):
    graphs += makeGraph(trailheads, start)

mainMap = {}
for g in graphs:
    for val, setPos in g.items():
        if val not in mainMap:
            mainMap[val] = setPos
        else:
            mainMap[val] = mainMap[val].union(setPos)

s = 0
for start in mainMap[0]:
    d = getDelta(trailheads, start, 1)
    val = 1
    print('Point de départ :', start)
    print('Nombre à verifier :', val)
    print(f'Positions possibles pour le nombre {val}: {d}')
    print("--------------------")
    while val != 9:
        dd = d.copy()
        d = set()
        for pos in dd:
            print(f'Position actuelle numéro {val}:', pos)
            delts = getDelta(trailheads, pos, val+1)
            print(f'Positions possibles pour le nombre {val+1}: {delts}')
            d = d.union(delts)
        val += 1
        print("--------------------")
    print("Nombre de chemins :", len(d))
    s += len(d)
    print(colored(f"Starting point: {start} | Number to verify: {val} | Number of paths: {len(d)}", 'green'))

print("Total number of paths:", s)