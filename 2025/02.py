def read_file() -> list[tuple[int, int]]:
    """
    Reads the file and returns it as a list of tuples of integers

    Returns:
        List of tuples containing the start and end of interals
    """
    intervals = []
    with open("2025/2.txt", "r") as f:
        for i in f:
            blocks = i.split(",")
            for bl in blocks:
                a, b = bl.split("-")
                intervals.append((int(a), int(b)))
            return intervals
        
def find_invalid(intervals: list[tuple[int, int]]) -> int:
    """
    Finds invalid integers inside the invervals. 
    An integer is invalid if it is in the format of XX where X is an integer

    Args:
        The intervals as a list of tuples

    Returns:
        The sum of invalid integers
    """
    total = 0
    for a, b in intervals:
        for num in range(a, b + 1):
            if len(str(num)) % 2 == 0:
                divi = 10 ** (len(str(num)) / 2)
                if (num // divi == num % divi):
                    total += num
    return total

def find_repeat(intervals: list[tuple[int, int]]) -> int:
    """
    Finds repeating invalid integers inside the invervals. 
    An integer is invalid if it is in the format of X * k where X is an integer, k is an integer > 1 -> XX, XXX, XXXX, XXXXX

    Args:
        The intervals as a list of tuples

    Returns:
        The sum of repeating invalid integers
    """
    total = 0
    for a, b in intervals:
        for num in range(a, b + 1):
            for length in range(1, len(str(num)) // 2 + 1):
                repeating = True
                if (len(str(num)) % length != 0):
                    continue
                i = length
                part = str(num)[0 : i]
                while i < len(str(num)):
                    if str(num)[i : i + length] != part:
                        repeating = False
                        break
                    i += length
                if repeating == True:
                    total += num
                    break
    return total
                


if __name__ == "__main__":
    intervals = read_file()
    print("Part 1:", find_invalid(intervals))
    print("Part 2:", find_repeat(intervals))