def read_file() -> list[int]:
    """
    Reads in numbers from the file, and stores them in a list

    Returns:
        The list of numbers
    """
    t = []
    with open("2024/13.txt","r") as f:
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


def reduced_echelon(t: list[int], higher: bool = False) -> int:
    """
    Takes the numbers by groups of 6, and using linear algebra calculates the number of tokens required

    Args: 
        t: The list of numbers
        higher: True if the prize amount should be increased by 10000000000000
    
    Returns:
        The total number of required tokens
    """
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
        
if __name__ == "__main__":
    t = read_file()
    print("Part 1:",reduced_echelon(t))
    print("Part 2:",reduced_echelon(t, higher = True))