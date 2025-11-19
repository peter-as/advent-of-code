def read_file() -> tuple[list[list[chr]], int, int]:
    """
    Reads in the a table from the file, and stores it as a list of list of characters
    Returns the table and the starting position of the guard

    Returns:
        A tuple of list of list of characters, and the indices of the guard
    """

    with open("2024/6.txt") as f:
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

def find_path(t: list[list[chr]], x: int, y: int) -> tuple[set[tuple[int, int]], bool]:
    """
    Finds the path the guard will take until it either loops or gets out of the map

    Args:
        t: The table
        x: the starting x index of the guard
        y: the starting y index of the guard

    Returns:
        A tuple of the set of tuples of coordinates of the locations the guard has visited, and a boolean true if the guard has looped
    """
    locations = set()
    direction = 0 # 0 : up, 1 : right, 2 : down, 3 : left
    n, m = len(t), len(t[0])
    i, j = x, y
    look = set()
    while i > 0 and j > 0 and i < n and j < m:
        locations.add((i, j))

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
            return locations, False
        if t[new_i][new_j] == "#":
            direction = (direction + 1) % 4
        else:
            if (i, j, direction) in look:
                return locations, True
            look.add((i, j, direction))
            i, j = new_i, new_j
    
    return locations, False

def put_obstacle(t: list[list[chr]], x: int, y: int, locations: list[tuple[int, int]]) -> int:
    """
    Goes through the locations, and checks how many coordinates, if obstructed would cause the guard to loop

    Args: 
        t: The table
        x: the starting x index of the guard
        y: the starting y index of the guard
        The list of tuples which could be obstructed

    Returns:
        The number of locations which when obstructed would cause the guard to loop
    """
    total = 0
    for i, j in locations:
        t[i][j] = "#"

        _, res = find_path(t, x, y)
        if res == True:
            total += 1
        t[i][j] = "."
    return total

if __name__ == "__main__":
    t,x,y = read_file()
    locations, _ = find_path(t, x, y)
    print("Part 1:", len(locations))
    print("Part 2:", put_obstacle(t, x, y, list(locations)))
