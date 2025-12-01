def read_file() -> list[tuple[chr, int]]:
    """
    Reads the file and stores the instructions as tuples of a character and an integer

    Returns:
        The list containing the instructions
    """
    t = []
    with open("2025/1.txt", "r") as f:
        for i in f:
            t.append((i[0], int(i[1:])))
    return t

def at_zero(t: list[tuple[chr, int]]) -> int:
    """
    Counts how many times the dial is at 0 after following an instruction

    Args:
        t: The list containing the instructions

    Returns:
        The number of times the dial was at 0 after an instruction
    """
    counter = 0
    dial = 50
    for d, r in t:
        if d == "L":
            dial -= r
        elif d == "R":
            dial += r
        while dial < 0:
            dial += 100
        dial = dial % 100
        if dial == 0:
            counter += 1
    return counter

def by_steps(t: list[tuple[chr, int]]) -> int:
    """
    Counts how many times the dial is at 0

    Args:
        t: The list containing the instructions

    Returns:
        The number of times the dial was at 0
    """
    counter = 0
    dial = 50
    for d, r in t:
        for i in range(r):
            if d == "L":
                dial -= 1
            elif d == "R":
                dial += 1
            if dial < 0:
                dial += 100
            dial = dial % 100
            if dial == 0:
                counter += 1
    return counter


if __name__ == "__main__":
    t = read_file()
    print("Part 1:", at_zero(t))
    print("Part 2:", by_steps(t))