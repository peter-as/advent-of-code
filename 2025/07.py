def read_file() -> list[str]:
    """
    Reads the file and stores it as a list of strings.

    Returns:
        The list of strings.
    """
    t = []
    with open("2025/7.txt", "r") as f:
        for i in f:
            t.append(i.split("\n")[0])
    return t

def split_beam(t: list[str]) -> int:
    """
    Simulates the travel and splitting of the beam, counting how many times it is split.

    Args:
        t: The list of strings representing the grid.

    Returns:
        The number of times the laser was split.
    """
    splits = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == "S" and i + 1 < len(t) and t[i][j + 1] == ".":
                t[i + 1] = t[i + 1][:j] + "|" + t[i + 1][j + 1:]
            elif t[i][j] == "." and i - 1 >= 0 and t[i - 1][j] == "|":
                t[i] = t[i][:j] + "|" + t[i][j + 1:]
            elif t[i][j] == "^" and i - 1 >= 0 and t[i - 1][j] == "|":
                split = False
                if j - 1 >= 0 and t[i][j - 1] == ".":
                    t[i] = t[i][:j - 1] + "|" + t[i][j:]
                    split = True
                if j + 1 < len(t[i]) and t[i][j + 1] == ".":
                    t[i] = t[i][:j + 1] + "|" + t[i][j + 2:]
                    split = True
                if split:
                    splits += 1
    return splits

def count_timelines(t: list[str]) -> int:
    """
    Checks the ways the beam has travelled, and counts how many total paths it could have taken.

     Args:
        t: The list of strings representing the simulated grid.

    Returns:
        The number of paths the laser took.
    """
    lines = {}
    for i in range(len(t)):
        for j in range(len(t[i])):
            lines[(i,j)] = 0 
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == "S":
                lines[(i, j)] = 1
                if i + 1 < len(t) and t[i + 1][j] == "|":
                    lines[(i + 1, j)] += 1
            elif t[i][j] == "|" and i - 1 >= 0 and t[i - 1][j] == "|":
                lines[(i, j)] += lines[(i - 1, j)]
            elif t[i][j] == "^" and i - 1 >= 0 and t[i - 1][j] == "|":
                if j - 1 >= 0 and t[i][j - 1] == "|":
                    lines[(i, j - 1)] += lines[(i - 1, j)]
                if j + 1 < len(t[i]) and t[i][j + 1] == "|":
                    lines[(i, j + 1)] += lines[(i - 1, j)]
    timelines = 0
    for j in range(len(t[-1])):
        timelines += lines[(len(t) - 1, j)]
    return timelines

if __name__ == "__main__":
    t = read_file()
    print("Part 1:", split_beam(t))
    print("Part 2:", count_timelines(t))