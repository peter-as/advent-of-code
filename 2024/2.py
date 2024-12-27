def readFile():
    f = open("2.txt","r")
    l = []
    for i in f:
        k = i.split()
        for p in range(len(k)):
            k[p] = int(k[p])
        l.append(k)
    return l

def check(l, index, inc):
    if l[index] == l[index - 1]:
        return False
    if l[index] > l[index - 1] and not inc:
        return False
    if l[index] < l[index - 1] and inc:
        return False
    if abs(l[index] - l[index - 1]) < 1 or abs(l[index] - l[index - 1]) > 3:
        return False
    return True

def validate(l, index, inc):
    if index >= len(l):
        return False
    valid = check(l, index, inc)
    if not valid:
        return False
    return True

def isSafe(l, inc):
    for i in range(1,len(l)):
        val = validate(l, i, inc)
        if val == False:
            return False
    return True

def analyze(l):
    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if isSafe(i, inc):
            safe += 1
    return safe

def analyzeWithError(l):
    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if isSafe(i, inc):
            safe+=1
        else:
            for k in range(len(i)):
                newL = i[:k] + i[k+1:]
                inc = False
                if (newL[1] > newL[0]):
                    inc = True
                if isSafe(newL, inc):
                    safe += 1
                    break
    return safe

nums = readFile()
print("Part 1:",analyze(nums))
print("Part 2:",analyzeWithError(nums))
