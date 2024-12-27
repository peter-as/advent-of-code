def read_file():

    f = open("15.txt","r")
    table = []
    steps = ""

    step = False
    for i in f:
        if i == "\n":
            step = True
            continue
        if step:
            steps += i.split()[0]
        else:
            row = []
            for l in i[:-1]:
                row.append(l)
            table.append(row)
    return table, steps

def find_robot(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "@":
                return (i,j)

def find_space(table, robot_x, robot_y , step_x, step_y):
    current_x, current_y = robot_x + step_x, robot_y + step_y
    while table[current_x][current_y] != "#":
        if table[current_x][current_y] == ".":
            return (current_x, current_y)
        current_x += step_x
        current_y += step_y
    return False
    

def simulate_steps(table, steps):
    robot_x, robot_y = find_robot(table)
    for step in steps:
        step_x,step_y = 0,0
        if step == "^":
            step_x -= 1
        elif step == "v":
            step_x += 1
        elif step == "<":
            step_y -= 1
        elif step == ">":
            step_y += 1
        
        if table[robot_x + step_x][robot_y + step_y] == ".":
            table[robot_x + step_x][robot_y + step_y] = "@"
            table[robot_x][robot_y] = "."
            robot_x += step_x
            robot_y += step_y
        else:
            space = find_space(table, robot_x, robot_y, step_x, step_y)
            if space == False:
                continue
            space_x, space_y = space[0], space[1]
            table[space_x][space_y] = "O"
            table[robot_x + step_x][robot_y + step_y] = "@"
            table[robot_x][robot_y] = "."
            robot_x += step_x
            robot_y += step_y
    return table

def gps_value(table):
    value = 0
    for i in range(1, len(table) - 1):
        for j in range(1, len(table[i]) - 1):
            if table[i][j] == "O":
                value += j + 100 * i

    return value

def visualize(table):
    for i in table:
        for j in i:
            print(j, end="")
        print()
    print()

table, steps = read_file()
#visualize(table)

moved_table = simulate_steps(table, steps)
#visualize(moved_table)

print("Part 1:", gps_value(table))


