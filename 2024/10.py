def read_file() -> tuple[list[str], list[tuple[int, int]]]:
    """
    Parse the file and store it in a list with padding. Also stores the indices of zeros

    Returns:
        A tuple of the table represented as a list of strings, and the indices of every zero as a list of tuples of integers

    """
    l = []
    zeros = []
    with open("2024/10.txt","r") as f:
        index = 0
        for i in f:
            i = i.split("\n")[0]
            for j in range(len(i)):
                if i[j] == "0":
                    zeros.append((index+1,int(j)+1))
            l.append("."+i+".")
            index += 1
        k = len(l[0])
        l.insert(0,k*".")
        l.append(k*".")
    return l, zeros

def check_all_neighbours(table: list[str], i: int, j: int) -> int:
    """
    Recursively finds every traversable trail from coordinates (i,j) by going to a higher elevation

    Args:
        table: The table represented as a list of strings
        i: The current x coordinate
        j: the current y coordinate

    Returns:
        The number of traversible trails from the current position
    """
    if table[i][j] == "9":
        return 1
    total = 0
    if not table[i-1][j] == "." and int(table[i-1][j]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i-1, j)
    if not table[i+1][j] == "." and int(table[i+1][j]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i+1, j)
    if not table[i][j-1] == "." and int(table[i][j-1]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i, j-1)
    if not table[i][j+1] == "." and int(table[i][j+1]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i, j+1)
    return total

def check_reachable_ends(table: list[str], i: int, j: int) -> set[tuple[int, int]]:
    """
    Recursively finds every 9 reachable from coordinates (i,j) by going to a higher elevation

    Args:
        table: The table represented as a list of strings
        i: The current x coordinate
        j: the current y coordinate

    Returns:
        The set of tuples of coordinates of the reachable 9s from the current position
    """
    if table[i][j] == "9":
        k = set()
        k.add((i,j))
        return k
    k = set()
    if not table[i-1][j] == "." and int(table[i-1][j]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i-1, j))
    if not table[i+1][j] == "." and int(table[i+1][j]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i+1, j))
    if not table[i][j-1] == "." and int(table[i][j-1]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i, j-1))
    if not table[i][j+1] == "." and int(table[i][j+1]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i, j+1))
    return k


def reachable_ends(table: list[str], zeros: list[tuple[int, int]]) -> int:
    """
    Counts how many 9s can be travelled to from the zeros

    Args:
        table: The table represented as a list of strings
        zeros: The coordinates of zeros represented as a list of tuples of integers
    """
    trails = 0
    for i, j in zeros:
        found = check_reachable_ends(table, i, j)
        trails += len(found)
    return trails   

def count_trails(table: list[str], zeros: list[tuple[int, int]]) -> int:
    """
    Counts how many hiking trails can be traversed from the zeros

    Args:
        table: The table represented as a list of strings
        zeros: The coordinates of zeros represented as a list of tuples of integers
    """
    trails = 0
    for i, j in zeros:
        found = check_all_neighbours(table, i, j)
        trails += found
    return trails        
    
if __name__ == "__main__":
    table, zeros = read_file()
    print("Part 1:", reachable_ends(table, zeros))
    print("Part 2:", count_trails(table, zeros))