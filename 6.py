def read_file():
    f = open("6.txt")
    t = []
    for i in f:
        t.append(i.split()[0])
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == "^":
                return t,i,j
    return 

def find_path(t,x,y):
    locations = set()
    direction = 0
    n = len(t)
    m = len(t[0])
    i = x
    j = y
    look = set()
    while i > 0 and j > 0 and i < n and j < m:
        locations.add((i,j))
        if direction == 0:
            if i - 1 < 0:
                return locations
            if t[i-1][j] == "#":
                direction = 1
            else:
                if (i,j,direction) in look:
                    return 0
                look.add((i,j,direction))
                i-=1
        if direction == 1:
            if j + 1 >= m:
                return locations
            if t[i][j+1] == "#":
                direction = 2
            else:
                if (i,j,direction) in look:
                    return 0
                look.add((i,j,direction))
                j+=1
        if direction == 2:
            if i + 1 >= n:
                return locations
            if t[i+1][j] == "#":
                direction = 3
            else:
                if (i,j,direction) in look:
                    return 0
                look.add((i,j,direction))
                i+=1
        if direction == 3:
            if j - 1 < 0:
                return locations
            if t[i][j-1] == "#":
                direction = 0
            else:
                if (i,j,direction) in look:
                    return 0
                look.add((i,j,direction))
                j-=1
    #return len(list(locations))

def put_obstacle(t,x,y):
    total = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == "^" or t[i][j] == "#":
                continue
            t[i] = t[i][:j]+"#"+t[i][j+1:]
            res = find_path(t,x,y)
            if res == 0:
                total += 1
            t[i] = t[i][:j]+"."+t[i][j+1:]
    return total

t,x,y = read_file()
sol = find_path(t,x,y)
print("Part 1:",len(sol))
print("Part 2:",put_obstacle(t,x,y))
