def readFile():
    # Read all the rows from the input as lists, and store them in a list

    f = open("2024/2.txt","r")
    l = []
    for i in f:
        k = i.split()
        for p in range(len(k)):
            k[p] = int(k[p])
        l.append(k)
    return l

def validate(l, index, inc):
    # I check multiple properties, returning False if any false

    if l[index] > l[index - 1] and not inc: # If the values are increasing but should be decreasing
        return False
    if l[index] < l[index - 1] and inc: # If the values are decreasing but should be increasing
        return False
    if abs(l[index] - l[index - 1]) < 1 or abs(l[index] - l[index - 1]) > 3: # If their difference is outside the range
        return False
    
    # Otherwise good
    return True

def isSafe(l, inc):
    # I iterate through the row starting from the second element
    #, and compare if the rule between this and previous element holds using validate()

    for i in range(1,len(l)):
        if not validate(l, i, inc):
            return False
    return True

def analyze(l):
    # I iterate through the rows, and first, I check if the numbers start increasing or decreasing, then call isSafe on the row

    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if isSafe(i, inc):
            safe += 1
    return safe

def analyzeWithError(l):
    # I iterate through the rows again, but now check if removing any of the elements of the row would make it good

    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if isSafe(i, inc): 
            safe += 1
        # Up until this point it is the same as the previous, but now if it's incorrect I try removing the elements
        else:
            for k in range(len(i)):
                # I remove the kth element, and see if it would pass as correct, if yes, I count it and moe on
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
