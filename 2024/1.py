def read_file() -> tuple[list[int], list[int]]:
    """
    Read a two column text file into list of integers.

    Returns:
        A tuple of two lists, where the lists contain the numbers from the two columns.
    """
    fir = []
    sec = []
    with open("2024/1.txt","r") as f:
        for i in f:
            k = i.split()
            fir.append(int(k[0]))
            sec.append(int(k[1]))
    return fir, sec

def difference(a: list[int], b: list[int]) -> int:
    """
    Calculates the difference between the respective values of the two columns
    
    Args:
        a: First list of integers
        b: Second list of integers

    Returns:
        The sum of the absolute difference for each pair in the list
    """
    total = 0
    for i,j in zip(a,b):
        total += abs(i-j)
    return total

def count_a_in_b(a: list[int], b: list[int]):
    """Calculate a weighted count of how often elements of the first column appear in the second column

    Args:
        a: First list of integers
        b: Second list of integers

    Returns:
        The sum over all elements of the first column
    
    """
    occur = {}
    for i in b:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    sum = 0
    for i in a:
        if i in occur:
            sum += i * occur[i]
    return sum

if __name__ == "__main__":
    column1, column2 = read_file()
    a, b = sorted(column1), sorted(column2)

    print("Part 1:",difference(a,b))
    print("Part 2:",count_a_in_b(a,b))