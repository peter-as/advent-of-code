def read_file():
    # I read the table from the input. I store them in two lists.
    # I store every character seperately
    # I return the table, and the starting position of the guard

    f = open("2024/6.txt")
    t = []
    for i in f:
        row = []
        for k in i.split()[0]:
            row.append(k)
        t.append(row)
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == "^":
                return t, i ,j
    return 

def find_path(t, x, y):
    # I find the path the guard takes from its starting position until it either leaves the map or gets in a loop

    locations = set() # A set to keep track of visited locations
    direction = 0 # The direction the guard faces 0 : up, 1 : right, 2 : down, 3 : left
    n, m = len(t), len(t[0])
    i, j = x, y
    look = set()
    while i > 0 and j > 0 and i < n and j < m: # We loop while we are inside the table
        locations.add((i, j)) # We add our location to the visited locations

        # We check the next step based on our direction
        # If we were to run into a wall, I turn right
        # Otherwise, I step forward, and add the guard's location and direction to "look"

        # Look is used in the second part. If something were to appear in it twice, it means the guard is in a loop
        # In this case, I return a 0

        new_i, new_j = i, j
        if direction == 0:
            new_i -= 1
        elif direction == 1:
            new_j += 1
        elif direction == 2:
            new_i += 1
        else:
            new_j -= 1
        
        if new_i < 0 or new_j < 0 or new_i >= n or new_j >= m:
            return locations
        if t[new_i][new_j] == "#":
            direction = (direction + 1) % 4
        else:
            if (i, j, direction) in look:
                return 0
            look.add((i, j, direction))
            i, j = new_i, new_j
    
    # Once the guard gets out of the table, I return the visited locations
    
    return locations

def put_obstacle(t,x,y,locations):
    # I check if I put an obstacle to a location, would that would cause a loop
    total = 0
    for i,j in locations:
        t[i][j] = "#"

        res = find_path(t,x,y) # If the guards gets in a loop, this will return a 0
        if res == 0:
            total += 1
        t[i][j] = "."
    return total

t,x,y = read_file()
sol = find_path(t, x, y)
print("Part 1:", len(sol))
print("Part 2:", put_obstacle(t, x, y, list(sol)))
