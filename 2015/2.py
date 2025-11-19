def read_file() -> list[tuple[int, int, int]]:
    """
    Reads the file and stores the measurements of the box as tuples in a list
    
    Returns:
        A list containing the measurements of the boxes in tuples
    """
    t = []
    with open("2015/2.txt", "r") as f:
        for i in f:
            i = i.split("x")
            t.append((int(i[0]), int(i[1]), int(i[2])))
    return t

def wrapping(measurements: list[tuple[int, int, int]]) -> int:
    """
    Calculates the amount of wrapping needed based on the box's dimensions

    Args:
        measurements: List containing the measurements of the box in tuples

    Returns:
        the total amount of wrapping needed
    """
    total = 0
    for a, b, c in measurements:
        sides = (a * b, a * c, b * c)
        total += sum(sides) * 2 + min(sides)
    return total

def ribbon(measurements: list[tuple[int, int, int]]) -> int:
    """
    Calculates the amount of ribbon needed based on the box's dimensions

    Args:
        measurements: List containing the measurements of the box in tuples

    Returns:
        the total amount of ribbon needed
    """
    total = 0
    for i in measurements:
        total += (sorted(i)[0] + sorted(i)[1]) * 2 + i[0] * i[1] * i[2]
    return total

if __name__ == "__main__":
    measurements = read_file()
    print("Part 1:", wrapping(measurements))
    print("Part 2:", ribbon(measurements))