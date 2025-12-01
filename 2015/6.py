def read_file() -> list[tuple[int, tuple[int, int]]]:
    """
    Reads the instructions into a tuple and stores them as a list

    Returns:
        List containing the instructions as tuples. The coordinates are stored in tuples, 
        the actions are represented as numbers: 0 - turn off, 1 - turn on, 2 - toggle
    """
    l = []
    with open("2015/6.txt", "r") as f:
        for i in f:
            parts = i.split()
            if len(parts) == 4:
                from_x, from_y = parts[1].split(',')
                to_x, to_y = parts[3].split(',')
                l.append((2, (int(from_x), int(from_y)), (int(to_x), int(to_y))))
            else:
                from_x, from_y = parts[2].split(',')
                to_x, to_y = parts[4].split(',')
                if (parts[1] == "on"):
                    l.append((1, (int(from_x), int(from_y)), (int(to_x), int(to_y))))
                else:
                    l.append((0, (int(from_x), int(from_y)), (int(to_x), int(to_y))))
    return l

def fill_dict() -> dict[(int, int), bool]:
    """
    Creates a dictionary representing the lights

    Returns:
        The dictionary where coordinates are the key, and the values are the light levels, represented as integers, by default 0
    """
    d = {}
    for i in range(0, 1000):
        for j in range(0, 1000):
            d[(i, j)] = 0
    return d

def toggle_light(instructions, lights, turn = False):
    total = 0
    for p in instructions:
        x1, y1 = p[1]
        x2, y2 = p[2]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if p[0] == 0:
                    lights[(i, j)] = max(0,lights[(i, j)] - 1) if turn else 0
                elif p[0] == 1:
                    lights[(i, j)] = lights[(i, j)] + 1 if turn else 1
                else:
                    lights[(i, j)] = lights[(i, j)] + 2 if turn else 1 - lights[(i, j)]
    for i in range(0, 1000):
        for j in range(0, 1000):
            total += lights[(i, j)]
    return total

if __name__ == "__main__":
    l = read_file()
    print("Part 1:", toggle_light(l, fill_dict()))
    print("Part 2:", toggle_light(l, fill_dict(), turn = True))