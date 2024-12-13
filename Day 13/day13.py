import sympy as sp

machines = []

with open('day13.txt', 'r', encoding='utf-8') as f:
    claw = {}
    for line in f:
        l = line.strip()
        # Si vide ou END, on ajoute la machine à la liste et on réinitialise claw
        if l == '' or l == 'END': # Ajoute END pour la dernière machine
            machines.append(claw)
            print(claw)
            claw = {}
        if 'A' in l:
            claw['A'] = []
            for x in l.split(': ')[1].split(', '):
                claw['A'].append(int(x.replace('X', ''))) if 'X' in x else claw['A'].append(int(x.replace('Y', '')))
        elif 'B' in l:
            claw['B'] = []
            for x in l.split(': ')[1].split(', '):
                claw['B'].append(int(x.replace('X', ''))) if 'X' in x else claw['B'].append(int(x.replace('Y', '')))
        elif 'Prize' in l:
            claw['out'] = []
            for x in l.split(': ')[1].split(', '):
                # claw['out'].append(int(x.replace('X=', ''))) if 'X' in x else claw['out'].append(int(x.replace('Y=', ''))) Part 1
                claw['out'].append(int(x.replace('X=', '')) + 10000000000000) if 'X' in x else claw['out'].append(int(x.replace('Y=', '')) + 10000000000000)
        else:
           continue

s = 0
for claw in machines:
    x, y = sp.symbols('x, y')
    A = claw['A']
    B = claw['B']
    output = claw['out']
    eqA = sp.Eq(A[0] * x + B[0] * y, output[0])
    eqB = sp.Eq(A[1] * x + B[1] * y, output[1])
    sol = sp.solve((eqA, eqB), (x, y))
    if isinstance(sol[x], sp.Integer) and isinstance(sol[y], sp.Integer): # and sol[x] < 100 and sol[y] < 100: # Part 1
        print(sol)
        print(type(sol[x]))
        s += (sol[x]*3) + (sol[y]*1)
        print((sol[x]*3) + (sol[y]*1), '->', s)
        print('------------')
    else:
        continue
    