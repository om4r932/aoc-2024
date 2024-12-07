graph = {}
series = []

with open('day5.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            t = line.split('|')
            if t[0] in graph:
                graph[t[0]].append(t[1])
            else:
                graph[t[0]] = [t[1]]
        elif ',' in line:
            series.append(line.split(','))

def ordon(s):
    newS = []
    test = s.copy()
    length = int(len(test))
    for i in range(0, length):
        newS.append(maximumCommonValues(test))
        test.remove(newS[i])
    return newS

def testSeries(series):
    somValid = 0
    somInvalid = 0
    for s in series:
        valid = True
        for x in s:
            ss = s.copy()
            ss.remove(x)
            for y in ss:
                if s.index(x) < s.index(y):
                    if x not in graph:
                        valid = False
                        continue
                    if y not in graph[x]:
                        valid = False
                else:
                    if y not in graph:
                        valid = False
                        continue
                    if x not in graph[y]:
                        valid = False
        print(s, valid)
        if valid:
            somValid += int(s[len(s) // 2])
        else:
            newS = ordon(s)
            somInvalid += int(newS[len(newS) // 2])
    return somValid, somInvalid

def commonValues(l1, l2):
    return list(set(l1) & set(l2))

def maximumCommonValues(serie):
    maxCommon = 0
    maxVal = serie[-1]
    for x in serie:
        serieCopy = serie.copy()
        serieCopy.remove(x)
        if x not in graph:
            continue
        common = len(commonValues(graph[x], serieCopy))
        if common > maxCommon:
            maxCommon = common
            maxVal = x
    return maxVal

print(testSeries(series))

