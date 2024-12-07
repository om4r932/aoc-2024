mapp = [] # Je n'ai pu faire uniquement la partie 1
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions = ['^', '>', 'v', '<']
with open('day6_test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        mapp.append([c for c in line.strip()])

def locateDriver(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j] in ['^', 'v', '<', '>']:
                return i, j

def changeDirection(mapp):
    driver_x, driver_y = locateDriver(mapp)
    driver = mapp[driver_x][driver_y]
    if driver == '^':
        mapp[driver_x][driver_y] = '>'
    elif driver == '>':
        mapp[driver_x][driver_y] = 'v'
    elif driver == 'v':
        mapp[driver_x][driver_y] = '<'
    elif driver == '<':
        mapp[driver_x][driver_y] = '^'

def getDirection(mapp):
    driver_x, driver_y = locateDriver(mapp)
    driver = mapp[driver_x][driver_y]
    if driver == '^':
        return 0
    if driver == '>':
        return 1
    if driver == 'v':
        return 2
    if driver == '<':
        return 3
            
def checkBox(mapp):
    driver_x, driver_y = locateDriver(mapp)
    dx, dy = deltas[getDirection(mapp)]
    if mapp[driver_x + dx][driver_y + dy] == '#' or mapp[driver_x + dx][driver_y + dy] == 'O':
        return True

def checkNextMoveOOB(mapp):
    driver_x, driver_y = locateDriver(mapp)
    dx, dy = deltas[getDirection(mapp)]
    if driver_x + dx < 0 or driver_x + dx >= len(mapp) or driver_y + dy < 0 or driver_y + dy >= len(mapp[0]):
        return True

def countX(mapp):
    c = 1
    for i in mapp:
        for j in i:
            if j == 'X':
                c += 1
    return c

while not checkNextMoveOOB(mapp):
    if checkBox(mapp):
        changeDirection(mapp)
    driver_x, driver_y = locateDriver(mapp)
    dx, dy = deltas[getDirection(mapp)]
    mapp[driver_x + dx][driver_y + dy] = mapp[driver_x][driver_y]
    mapp[driver_x][driver_y] = 'X'

