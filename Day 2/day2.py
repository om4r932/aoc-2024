reports = []
safe_reports = 0
with open('day2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        r = line.strip().split(' ')
        reports.append([int(x) for x in r])

# Part 1

def continualSeries(l, mode = "", p = False):
    def error(): # Fonction de texte si erreur
        return "Trop valeur" if abs(l[0] - l[1]) > 3 else "Signe"
    if len(l) <= 1:
        return True # Cas par défaut
    elif mode == "": # Cas initial (premier élément)
        if l[0] > l[1] and abs(l[0] - l[1]) >= 1 and abs(l[0] - l[1]) <= 3:
            return continualSeries(l[1:], ">") # Initialise mode pour les tests
        elif l[0] < l[1] and abs(l[0] - l[1]) >= 1 and abs(l[0] - l[1]) <= 3:
            return continualSeries(l[1:], "<") # Idem
        else: # Si égal
            print(l[0], l[1], abs(l[0] - l[1]), error()) if p else None
            return False
    elif mode == ">":
        if l[0] > l[1] and abs(l[0] - l[1]) >= 1 and abs(l[0] - l[1]) <= 3: # Vérifie la continuité
            return continualSeries(l[1:], ">")
        else:
            print(l[0], l[1], abs(l[0] - l[1]), mode, error()) if p else None
            return False
    elif mode == "<":
        if l[0] < l[1] and abs(l[0] - l[1]) >= 1 and abs(l[0] - l[1]) <= 3: # Vérifie également la continuité
            return continualSeries(l[1:], "<")
        else:
            print(l[0], l[1], abs(l[0] - l[1]), mode, error()) if p else None
            return False

for report in reports:
    if continualSeries(report):
        safe_reports += 1

print(safe_reports)

# Part 2

safe_reports = 0

def continualSeriesWithSingleBadLevel(l, mode = "", p = False):
    def error():
        return "Trop valeur" if abs(l[0] - l[1]) > 3 else "Signe"
    if len(l) <= 1:
        return True
    for case in range(len(l)): # Pour chaque liste, crée une copie sans l'élément, puis lance la fonction de la partie 1 avec celle-ci
        ll = l.copy()
        ll.pop(case)
        if continualSeries(ll):
            return True
    return False

for report in reports:
    if continualSeriesWithSingleBadLevel(report):
        safe_reports += 1

print(safe_reports)