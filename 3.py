def openFile():
    f = open("3.txt","r")
    l = []
    for i in f:
        l.append(i)
    return l

def multIndices(s):
    indices = []
    for i in range(len(s)):
        if s[i:min(i+3,len(s))] == "mul":
            indices.append(i)
    return indices

def multIndicesWithEnabling(s, enabled = True):
    indices = []
    for i in range(len(s)):
        if s[i:min(i+3,len(s))] == "mul" and enabled:
            indices.append(i)
        elif s[i:min(i+7,len(s))] == "don't()":
            enabled = False
        elif s[i:min(i+4,len(s))] == "do()":
            enabled = True
            
    return indices, enabled

def analyzeMul(s,i,indices):
    j = indices[i] + 3
    nums = set(["0","1","2","3","4","5","6","7","8","9"])
    end = len(s)
    step = 0
    first = ""
    second = ""
    if i < len(indices)-1:
        end = indices[i+1]
    while j < end:
        if step == 0:
            if s[j] == '(':
                step = 1
                j += 1
                continue
            else:
                return 0
        if step == 1:
            if s[j] not in nums:
                step = 2
            else:
                first += s[j]

        if step == 2:
            if s[j] == ',':
                step = 3
                j += 1
                continue
            else:
                return 0
        if step == 3:
            if s[j] not in nums:
                step = 4
            else:
                second += s[j]
        if step == 4:
            if not s[j] == ')':
                return 0
            else:
                return int(first) * int(second)
        j += 1
    return 0
        

def addMult(list, enabling = False):
    sum = 0
    enabled = True
    for string in list:
        if enabling:
            indices, enabled = multIndicesWithEnabling(string, enabled)
        else:
            indices = multIndices(string)
        for i in range(len(indices)):
            sum += analyzeMul(string,i,indices)
        
    return sum
    
l = openFile()
print("Part 1:",addMult(l))
print("Part 2:",addMult(l,True))
