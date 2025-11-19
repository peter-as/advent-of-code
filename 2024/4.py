def read_input() -> list[str]:
    """
    Reads in a table of characters as a list of strings

    Returns:
        The read list of strings
    """
    with open("2024/4.txt","r") as f:
        return [x for x in f]

def create_padding(l: list[str]) -> list[str]:
    """
    Creates padding for the table, by putting 3 rows and columns of "#" around the table

    Args:
        l: the table of strings
    
    Returns:
        The padded table of strings
    """
    n = len(l)
    m = len(l[0])
    s = "#" * (m + 6)
    for i in range(n):
        l[i] = "###" + l[i] + "###"
    for i in range(3):  
        l.insert(0, s)
        l.append(s)
    return l

def find_xmas(l: list[str]) -> int:
    """
    Finds every instance of 'XMAS' in the table
    Finds every 'X', and then checks the 8 directions if they line up to 'XMAS'

    Args:
        l: The table of strings

    Returns:
        The number of 'XMAS'
    """
    xmas = 0
    for i in range(3, len(l) - 3):
        for j in range(3, len(l[i]) - 3):
            if l[i][j] == "X":
                up_left = l[i][j] + l[i-1][j-1] + l[i-2][j-2] + l[i-3][j-3]
                up = l[i][j] + l[i-1][j] + l[i-2][j] + l[i-3][j]
                up_right = l[i][j] + l[i-1][j+1] + l[i-2][j+2] + l[i-3][j+3]
                right = l[i][j] + l[i][j+1] + l[i][j+2] + l[i][j+3]
                down_right = l[i][j] + l[i+1][j+1] + l[i+2][j+2] + l[i+3][j+3]
                down = l[i][j] + l[i+1][j] + l[i+2][j] + l[i+3][j]
                down_left = l[i][j] + l[i+1][j-1] + l[i+2][j-2] + l[i+3][j-3]
                left = l[i][j] + l[i][j-1] + l[i][j-2] + l[i][j-3]
                xmas += [up_left, up, up_right, right, down_right, down, down_left, left].count("XMAS")
    return xmas

def find_mas(l: list[str]) -> int:
    """
    Finds every cross, that is 2 'MAS'
    Finds every 'A', and checks the crosses if they spell out 'MAS' 2 times

    Args:
        l: The table of strings

    Returns:
        The number of cross 'MAS'-es
    """
    mas = 0
    for i in range(3, len(l) - 3):
        for j in range(3, len(l[i]) - 3):
            if l[i][j] == "A":
                up_left = l[i-1][j-1] + l[i][j] + l[i+1][j+1]
                up_right = l[i-1][j+1] + l[i][j] + l[i+1][j-1]
                down_right = l[i+1][j+1] + l[i][j] + l[i-1][j-1]
                down_left = l[i+1][j-1] + l[i][j] + l[i-1][j+1]
                mas += 1 if [up_left, up_right, down_right, down_left].count("MAS") == 2 else 0
    return mas

if __name__ == "__main__":
    l = create_padding(read_input())
    print("Part 1:", find_xmas(l))
    print("Part 2:", find_mas(l))
