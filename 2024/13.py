def read_file():
    f = open("13.txt","r")
    t = []
    for i in f:
        if i == "\n":
            continue
        k = i.split(": ")[1]
        if i[0] == "B":
            l = k.split("+")
            t.append(int(l[1].split(",")[0]))
            t.append(int(l[2]))
        else:
            l = k.split("=")
            t.append(int(l[1].split(",")[0]))
            t.append(int(l[2]))
    return t


def reduced_echelon(t, higher = False):
    steps = 0
    for i in range(0,len(t),6):
        x0,x1,x_f,y0,y1,y_f = t[i],t[i+2],t[i+4],t[i+1],t[i+3],t[i+5]
        if higher:
            x_f += 10000000000000
            y_f += 10000000000000

        A = (x1 * y_f - y1 * x_f) / (x1 * y0 - y1 * x0)
        B = (x_f - x0 * A) / x1
        if abs(A - round(A)) < 0.001 and abs(B - round(B)) < 0.001:
            steps += int(3*A + B)

        
    return steps
        

t = read_file()
print("Part 1:",reduced_echelon(t))
print("Part 2:",reduced_echelon(t,True))
            
