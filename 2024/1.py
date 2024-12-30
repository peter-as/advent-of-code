def readFile():
    # Read the input into two lists, to store the first and second columns respectively

    f = open("2024/1.txt","r")
    fir = []
    sec = []
    for i in f:
        k = i.split()
        fir.append(int(k[0]))
        sec.append(int(k[1]))
    return (fir, sec)

def difference(a, b):
    # Now I calculate the difference between the respective values of the two columns
    sum = 0
    for i,j in zip(a,b):
        sum += abs(i-j)
    return sum

def countAinB(a, b):
    # I create a dictionary to store how many times a number has appeared in the second column
    occur = {}
    for i in b:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    # Now I go over the first column and use the number of appearences of the number instead
    sum = 0
    for i in a:
        if i in occur:
            sum += i * occur[i]
    return sum

nums = readFile()
a, b = sorted(nums[0]), sorted(nums[1]) # I sort the two columns

print("Part 1:",difference(a,b))
print("Part 2:",countAinB(a,b))
