def read_file() -> str:
    """
    Reads the instructions from the file as a string

    Returns:
        The instructsions as a string
    """
    with open("2015/3.txt", "r") as f:
        for i in f:
            return i

def houses(instructions: str) -> set[(int, int)]:
    """
    Calculates coordinates of houses visited by following the instructions

    Args:
        instructions: String containing the instructions to follow

    Returns:
        Set containing the coordinates of the visited houses
    """
    locations = set()
    locations.add((0, 0))
    x, y = 0, 0
    for i in instructions:
        if i == '^':
            y += 1
        elif i == 'v':
            y -= 1
        elif i == '<':
            x -= 1
        elif i == '>':
            x += 1
        locations.add((x, y))
    return locations

def double_houses(instructions: str) -> set[(int, int)]:
    """
    Calculates coordinates of houses visited by two santas moving consecutively, following the instructions

    Args:
        instructions: String containing the instructions to follow

    Returns:
        Set containing the coordinates of the visited houses
    """
    locations = set()
    locations.add((0, 0))
    x, y, x2, y2 = 0, 0, 0, 0
    
    human = True
    for i in instructions:
        if i == '^':
            y, y2 = (y + 1, y2) if human else (y, y2 + 1)
        elif i == 'v':
            y, y2 = (y - 1, y2) if human else (y, y2 - 1)
        elif i == '<':
            x, x2 = (x - 1, x2) if human else (x, x2 - 1)
        elif i == '>':
            x, x2 = (x + 1, x2) if human else (x, x2 + 1)
        
        human = not human
        locations.add((x, y))
        locations.add((x2, y2))
    return locations


if __name__ == "__main__":
    instructions = read_file()
    print("Part 1:", len(houses(instructions)))
    print("Part 2:", len(double_houses(instructions)))