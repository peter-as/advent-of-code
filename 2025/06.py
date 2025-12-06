def read_file() -> list[str]:
    """
    Reads the numbers and symbols from the file and stores them as strings with the spaces.

    Returns:
        The list of strings.
    """
    t = []
    with open("2025/6.txt", "r") as f:
        for i in f:
            t.append(i.split("\n")[0])
    return t

def do_math(t: list[str]) -> int:
    """
    Turns the strings into numbers and does calculations with the numbers in a column.

    Args:
        t: The list of strings.

    Returns:
        The sum of the calculations.
    """
    total = 0
    for j in range(len(t[0])):
        numbers = []
        for i in range(len(t) - 1):
            numbers.append(int(t[i][j]))
        if t[-1][j] == "+":
            result = 0
            for n in numbers:
                result += n
        elif t[-1][j] == "*":
            result = 1
            for n in numbers:
                result *= n
        total += result
    return total

def do_math_column(t: list[str]) -> int:
    """
    Takes the digits column-wise and turns them into numbers then does the operations.

    Args:
        t: The list of strings.

    Returns:
        The sum of the calculations.
    """
    total = 0
    symbols = t[-1].split()
    calculation = 0
    numbers = []
    for i in range(len(t)):
        t[i] = t[i] + " "
    for j in range(len(t[0])):
        n = ""
        for i in range(len(t) - 1):
            n += t[i][j]    
        if (n == " " * len(n)):
            result = 0
            if symbols[calculation] == "+":
                result = 0
                for n in numbers:
                    result += n
                total += result
            elif symbols[calculation] == "*":
                result = 1
                for n in numbers:
                    result *= n
                total += result
            calculation += 1
            numbers = []
        else:
            numbers.append(int(n))
    return total

if __name__ == "__main__":
    t = read_file()
    print("Part 1:", do_math([x.split() for x in t]))
    print("Part 2:", do_math_column(t))