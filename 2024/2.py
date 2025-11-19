def readFile() -> list[list[int]]:
    """
    Read rows of lists of integers from a file, and store it in a list of list of integers.

    Returns:
        A list of list of integers.
    """
    l = []
    with open("2024/2.txt","r") as f:
        for i in f:
            k = i.split()
            for p in range(len(k)):
                k[p] = int(k[p])
            l.append(k)
    return l

def validate(l: list[int], index: int, inc: bool) -> bool:
    """
    Checks if the pair of values are safe, by checking if they follow the increasing rule, and if their difference are below or 3

    Args:
        l: The list of integers
        index: the index if the number we check in the list
        inc: Should the values be increasing or decreasing

    Returns:
        Are the two values following the rule
    """
    if l[index] > l[index - 1] and not inc: # If the values are increasing but should be decreasing
        return False
    if l[index] < l[index - 1] and inc: # If the values are decreasing but should be increasing
        return False
    if abs(l[index] - l[index - 1]) < 1 or abs(l[index] - l[index - 1]) > 3: # If their difference is outside the range
        return False
    
    # Otherwise good
    return True

def is_safe(l: list[int], inc: bool) -> bool:
    """
    Check if the row of numbers are safe, by checking the validity between each pair of numbers
    
    Args:
        l: The list of integers
        inc: Was the first two numbers increasing or decreasing

    Returns:
        If the row is safe
    """

    for i in range(1,len(l)):
        if not validate(l, i, inc):
            return False
    return True

def analyze(l: list[list[int]]) -> int:
    """
    Iterate through every row, and check if they start increasing or decreasing, then call is_safe to check if the row is safe

    Args:
        l: The list of list of integers

    Returns:
        The number of safe rows
    """
    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if is_safe(i, inc):
            safe += 1
    return safe

def analyzeWithError(l: list[list[int]]) -> int:
    """
    Iterate through every row, check if they start increasing or not, then check if the row is safe. 
    If not, check if it could be safe by removing an element

    Args:
        l: The list of list of integers
    
    Returns:
        The number of safe rows
    """
    safe = 0
    for i in l:
        inc = False
        if (i[1] > i[0]):
            inc = True
        if is_safe(i, inc): 
            safe += 1

        else:
            for k in range(len(i)):
                # I remove the kth element, and see if it would pass as correct, if yes, I count it and move on
                newL = i[:k] + i[k+1:]
                inc = False
                if (newL[1] > newL[0]):
                    inc = True
                if is_safe(newL, inc):
                    safe += 1
                    break
    return safe

if __name__ == "__main__":
    nums = readFile()
    print("Part 1:",analyze(nums))
    print("Part 2:",analyzeWithError(nums))
