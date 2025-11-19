def open_file() -> list[str]:
    """
    Read in multiple strings, and add them to a list

    Returns:
        The list of strings
    """
    l = []
    with open("2024/3.txt","r") as f:
        for i in f:
            l.append(i)
        return l

def mult_indices(s: str) -> list[int]:
    """
    Loops through the string, and if the next three characters are 'mul' it saves the current index

    Args:
        s: The string

    Returns:
        The list of indices where 'mul' appears
    """
    indices = []
    for i in range(len(s)):
        if s[i:min(i+3,len(s))] == "mul":
            indices.append(i)
    return indices

def mult_indices_with_enabling(s: str, enabled: bool = True) -> tuple[list[int], bool]:
    """
    Loops through the string, and if the next three characters are 'mul' it saves the current index
    It it sees 'don't()' it will stop recognising 'mul' until there is a 'do()'

    Args:
        s: The string
        enabled: Can 'mul' currently be recognised

    Returns:
        A tuple of the list of indices where 'mul' appears, and the current state of enabled
    """
    indices = []
    for i in range(len(s)):
        if s[i:min(i+3,len(s))] == "mul" and enabled:
            indices.append(i)
        elif s[i:min(i+7,len(s))] == "don't()":
            enabled = False
        elif s[i:min(i+4,len(s))] == "do()":
            enabled = True
            
    return indices, enabled

def analyze_mul(s: str, j: int) -> int:
    """
    Checks if the 'mul' is correct, and then calculates its value
    It should consist of "(", numbers, "," numbers, ")"     
    
    Args:
        s: the string the 'mul' is in
        j: the first character after the 'mul'

    Returns:
        The value of the multiplication if it is correct, otherwise 0
    """
    nums = set(["0","1","2","3","4","5","6","7","8","9"])
    end = len(s)
    step = 0 # Currenet status
    first = "" # The first number
    second = "" # The second number
    while j < end:
        if step == 0: # If I am in step 0, I should get a "(" next, if no, "mul" is incorrect
            if s[j] == '(':
                step = 1
                j += 1
                continue
            else:
                return 0
        if step == 1: # If I am in step 1, I should see a number, which I store. If not, I go to step 2
            if s[j] not in nums:
                step = 2
            else:
                first += s[j]

        if step == 2: # If I am in step 2, I should get a ",", if no, "mul" is incorrect
            if s[j] == ',':
                step = 3
                j += 1
                continue
            else:
                return 0
        if step == 3: # If I am in step 3, I should see a number, which I store. If not, I go to step 4
            if s[j] not in nums:
                step = 4
            else:
                second += s[j]
        if step == 4: # If I are in step 4, I should get a ")", if no, "mul" is incorrect
            if not s[j] == ')':
                return 0
            else:
                return int(first) * int(second) # I have successfully found a good "mul" with 2 numbers
        j += 1
    return 0
        

def add_mult(l: list[str], enabling = False) -> int:
    """
    Iterate through the strings, and find every instance of 'mul'.
    If enabling is on, then only those will be retrieved that are enabled.
    Every mul will be checked for correctness, then the multiplication is calculated and summed

    Args:
        l: The list of strings
        enabling: can 'mul's be disabled
    
    Returns:
        The sum of multiplications
    """
    sum = 0
    enabled = True
    for string in l:
        if enabling:
            indices, enabled = mult_indices_with_enabling(string, enabled)
        else:
            indices = mult_indices(string)
        for i in range(len(indices)):
            sum += analyze_mul(string, indices[i] + 3)
        
    return sum

if __name__ == "__main__":
    l = open_file()
    print("Part 1:",add_mult(l))
    print("Part 2:",add_mult(l, enabling = True))
