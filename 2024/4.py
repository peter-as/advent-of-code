def read_input():
    # Read all the rows from the input, and save them as seperate strings

    f = open("2024/4.txt","r")
    return [x for x in f]

def create_padding(l):
    # I pad the input, by surrounding the table with 3 "#"s, to make sure there are no indexing issues
    n = len(l)
    m = len(l[0])
    s = "#" * (m + 6)
    for i in range(n):
        l[i] = "###" + l[i] + "###"
    for i in range(3):  
        l.insert(0, s)
        l.append(s)
    return l

def find_xmas(l):
    # I go through the whole table, and for every cell I check if it could be the part of an XMAS by checking all 8 directions

    xmas = 0
    for i in range(3, len(l) - 3):
        for j in range(3, len(l[i]) - 3):
            if l[i][j] == "X":
                up_left = l[i][j] + l[i-1][j-1] + l[i-2][j-2] + l[i-3][j-3]
                up = l[i][j] + l[i-1][j] + l[i-2][j] + l[i-3][j]
                up_right = l[i][j] + l[i-1][j+1] + l[i-2][j+2] + l[i-3][j+3]
                right = l[i][j] + l[i][j+1] + l[i][j+2] + l[i][j+3]
                down_right = l[i][j] + l[i+1][j+1] + l[i+2][j+2] + l[i+3][j+3]
                down = l[i][j] + l[i+1][j] + l[i+2][j] + l[i+3][j]
                down_left = l[i][j] + l[i+1][j-1] + l[i+2][j-2] + l[i+3][j-3]
                left = l[i][j] + l[i][j-1] + l[i][j-2] + l[i][j-3]
                xmas += [up_left, up, up_right, right, down_right, down, down_left, left].count("XMAS")
    return xmas

def find_mas(l):
    # I go through the whole table, and for every cell I check if it could be the center of a "MAS". Then I check if I have 2

    mas = 0
    for i in range(3, len(l) - 3):
        for j in range(3, len(l[i]) - 3):
            if l[i][j] == "A":
                up_left = l[i-1][j-1] + l[i][j] + l[i+1][j+1]
                up_right = l[i-1][j+1] + l[i][j] + l[i+1][j-1]
                down_right = l[i+1][j+1] + l[i][j] + l[i-1][j-1]
                down_left = l[i+1][j-1] + l[i][j] + l[i-1][j+1]
                mas += 1 if [up_left, up_right, down_right, down_left].count("MAS") == 2 else 0
    return mas


l = create_padding(read_input())
print("Part 1:", find_xmas(l))
print("Part 2:", find_mas(l))
