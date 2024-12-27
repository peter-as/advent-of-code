def readFile():

    f = open("1.txt","r")
    fir = []
    sec = []
    for i in f:
        k = i.split()
        fir.append(int(k[0]))
        sec.append(int(k[1]))
    return (fir, sec)

def difference(a, b):
    sum = 0
    for i,j in zip(a,b):
        sum += abs(i-j)
    return sum

def countAinB(a, b):
    occur = {}
    for i in b:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    sum = 0
    for i in a:
        if i in occur:
            sum += i * occur[i]
    return sum

nums = readFile()
a, b = sorted(nums[0]), sorted(nums[1])

print("Part 1:",difference(a,b))
print("Part 2:",countAinB(a,b))
