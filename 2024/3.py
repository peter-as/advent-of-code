def openFile():
    # Read all the rows from the input, and save them as seperate strings

    f = open("2024/3.txt","r")
    l = []
    for i in f:
        l.append(i)
    return l

def multIndices(s):
    # If a the next three characters form a "mul", I save its index
    
    indices = []
    for i in range(len(s)):
        if s[i:min(i+3,len(s))] == "mul":
            indices.append(i)
    return indices

def multIndicesWithEnabling(s, enabled = True):
    # If a the next three characters form a "mul", I save its index
    # I also keep track if I see a "don't()", and then not consider "muls" until a "do()" 

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
    j = indices[i] + 3 # The index of the first number's first characters
    nums = set(["0","1","2","3","4","5","6","7","8","9"]) # The possible characters for numbers
    end = len(s) # The end of the row, there are no more characters past this
    step = 0 # To track where I am in processing the string
    first = "" # The first number
    second = "" # The second number
    while j < end: # While I can still step
        if step == 0: # If I am in step 0, I should get a "(" next, if no, "mul" is incorrect
            if s[j] == '(':
                step = 1
                j += 1
                continue
            else:
                return 0
        if step == 1: # If I am in step 1, I should see a number, which I store. If not, I go to step 2
            if s[j] not in nums:
                step = 2
            else:
                first += s[j]

        if step == 2: # If I am in step 2, I should get a ",", if no, "mul" is incorrect
            if s[j] == ',':
                step = 3
                j += 1
                continue
            else:
                return 0
        if step == 3: # If I am in step 3, I should see a number, which I store. If not, I go to step 4
            if s[j] not in nums:
                step = 4
            else:
                second += s[j]
        if step == 4: # If I are in step 4, I should get a ")", if no, "mul" is incorrect
            if not s[j] == ')':
                return 0
            else:
                return int(first) * int(second) # I have successfully found a good "mul" with 2 numbers
        j += 1
    return 0
        

def addMult(list, enabling = False):
    # I look through the rows, and calculate the final value

    sum = 0
    enabled = True
    for string in list:
        # In the first part, I gather every mul in the row

        if enabling: # If I am doing Part 2, I use another version where I discard "muls" if they are disabled
            indices, enabled = multIndicesWithEnabling(string, enabled)
        else:
            indices = multIndices(string) 
        for i in range(len(indices)): # After I have all the right "mul" indices, I calculate the result
            sum += analyzeMul(string,i,indices)
        
    return sum
    
l = openFile()
print("Part 1:",addMult(l))
print("Part 2:",addMult(l,True))
