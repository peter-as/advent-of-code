def read_file() -> str:
    """
    Reads the file as a string

    Returns:
        A string consisting of the brackets
    """
    with open("2015/1.txt", "r") as f:
        for i in f:
            return i
        
def travel(instructions: str) -> int:
    """
    Follows the instructions to calculate the final level

    Args:
        instructions: The string containing the characters saying if you have to go up or down

    Returns:
        The final floor
    """
    level = 0
    for i in instructions:
        if i == '(':
            level += 1
        elif i == ')':
            level -= 1
    return level

def basement(instructions: str) -> int:
    """
    Finds the position of the first instruction that makes the floor -1

    Args:
        instructions: The string containing the characters saying if you have to go up or down

    Returns:
        The position of the instruction that makes the floor -1
    """
    level = 0
    index = 0
    for i in instructions:
        index += 1
        if i == '(':
            level += 1
        elif i == ')':
            level -= 1
        
        if level == -1:
            return index
    return -1

if __name__ == "__main__":
    instructions = read_file()
    print("Part 1:", travel(instructions))
    print("Part 2:", basement(instructions))