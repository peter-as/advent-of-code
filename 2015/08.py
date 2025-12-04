def read_file() -> list[str]:
    """
    Reads the file and stores it as a list of strings.

    Returns the list of strings.
    """
    t = []
    with open("2015/8.txt", "r") as f:
        for i in f:
            t.append(i.split("\n")[0])
    return t

def decode(t: list[str]) -> int:
    """
    Decodes the strings and gives how much shorter they are than the string literal.

    Args:
        t: The list of strings

    Returns:
        The size the decoded strings are shorter by.
    """
    total = 0
    for row in t:
        i = 1
        counter = 0
        while i < len(row) - 1:
            if row[i] == "\\":
                if (row[i + 1] == "x"):
                    i += 4
                else:
                    i += 2
            else:
                i += 1
            counter += 1
        total += len(row) - counter
    return total

def encode(t: list[str]) -> int:
    """
    Encodes the strings and gives how much longer they are than the string literal.

    Args:
        t: The list of strings

    Returns:
        The size the decoded strings are longer by.
    """
    total = 0
    for row in t:
        i = 0
        counter = 2
        while i < len(row):
            if row[i] == "\\" or row[i] == "\"":
                counter += 1
            i += 1
            counter += 1
        total += counter - len(row)
    return total

if __name__ == "__main__":
    t = read_file()
    print("Part 1:", decode(t))
    print("Part 2:", encode(t))