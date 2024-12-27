def read_input():
    f = open("4.txt","r")
    return [x for x in f]

def create_padding(l):
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
    xmas = 0
    d = {"ul": 0, "u": 0, "ur": 0, "r": 0, "dr": 0, "d": 0, "dl": 0, "l":0}
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
                if up_left == "XMAS":
                    d["ul"] += 1
                if up == "XMAS":
                    d["u"] += 1
                if up_right == "XMAS":
                    d["ur"] += 1
                if right == "XMAS":
                    d["r"] += 1
                if down_right == "XMAS":
                    d["dr"] += 1
                if down == "XMAS":
                    d["d"] += 1
                if down_left == "XMAS":
                    d["dl"] += 1
                if left == "XMAS":
                    d["l"] += 1
                xmas += [up_left, up, up_right, right, down_right, down, down_left, left].count("XMAS")
    k = {"up-left": d["ul"], "up": d["u"], "up-right": d["ur"], "right": d["r"], "down-right": d["dr"], "down": d["d"], "down-left": d["dl"], "left": d["l"]}
    print(k)
    return xmas

def find_mas(l):
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
