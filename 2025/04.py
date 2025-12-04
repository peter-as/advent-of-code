def read_file() -> list[str]:
    """
    Reads the table from the file as a list of string.
    Surrounds the table with padding.

    Returns:
        The table as a list of strings.
    """
    t = []
    with open("2025/4.txt", "r") as f:
        for i in f:
            t.append("." + i.split("\n")[0] + ".")
    padding = "." * len(t[0])
    t.append(padding)
    t.insert(0, padding)
    return t

def find_movable(t: list[str]) -> list[tuple[int, int]]:
    """
    Finds movable boxes (the ones that have less than 8 boxes in their vicinity).

    Args:
        t: The table as a list of strings.

    Returns:
        The indices of the boxes that are movable.
    """
    movable = []
    for i in range (1, len(t) - 1):
        for j in range(1, len(t[i]) - 1):
            if t[i][j] == "@":
                neighbours = (
                    t[i - 1][j - 1], t[i - 1][j], t[i - 1][j + 1],
                    t[i][j - 1],                     t[i][j + 1],
                    t[i + 1][j - 1], t[i + 1][j], t[i + 1][j + 1])
                boxes = 0
                for n in neighbours:
                    if n == "@":
                        boxes += 1
                if boxes < 4:
                    movable.append((i, j))
    return movable

def find_all_movable(t: list[str]) -> int:
    """
    Finds and removes all the movable boxes.

    Args:
        t: The table as a list of strings.

    Returns:
        The number of boxes that were movable/
    """
    total = 0
    movable = find_movable(t)
    while len(movable) > 0:
        total += len(movable)
        for i, j in movable:
            t[i] = t[i][:j] + "." + t[i][j + 1:]
        movable = find_movable(t)
    return total

if __name__ == "__main__":
    t = read_file()
    print("Part 1:", len(find_movable(t)))
    print("Part 2:", find_all_movable(t))