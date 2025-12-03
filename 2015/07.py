import copy

def read_file() -> list[tuple[tuple[str, str, str], str]]:
    """
    Reads the file and stores the instructions as tuples, 
    where the first element is a tuple containing the left side of the operation,
    and the right side is the result wire.

    Returns:
        The list containing the instructions.
    """
    t = []
    with open("2015/7.txt", "r") as f:
        for i in f:
            i = i.split("\n")[0]
            action, result = i.split(" -> ")
            if "NOT" in action:
                not_what = action.split(" ")[1]
                t.append((("NOT", not_what, "EMPTY"), result))
            elif "AND" in action:
                a, b = action.split(" ")[0], action.split(" ")[2]
                t.append((("AND", a, b), result))
            elif "OR" in action:
                a, b = action.split(" ")[0], action.split(" ")[2]
                t.append((("OR", a, b), result))
            elif "LSHIFT" in action:
                a, b = action.split(" ")[0], action.split(" ")[2]
                t.append((("LSHIFT", a, b), result))
            elif "RSHIFT" in action:
                a, b = action.split(" ")[0], action.split(" ")[2]
                t.append((("RSHIFT", a, b), result))
            elif action.isnumeric():
                t.append((("NUM", action, "EMPTY"), result))
            else:
                t.append((("LIT", action, "EMPTY"), result))
    return t

def remove_singles(t: list[tuple[tuple[str, str, str], str]]) -> dict[str, int]:
    """
    Processes literal and number operations, and stores their values in a dictionary.
    
    Args:
        t: The list containing the instructions.

    Returns:
        Dictionary containing some wires and their corresponding values.
    """
    i = 0
    while i < len(t):
        action, result = t[i]
        if action[0] == "LIT":
            fr, to = action[1], result
            for l in range(len(t)):
                actionIN, resultIN = t[l]
                a, b = actionIN[1], actionIN[2]
                if actionIN[1] == fr:
                    a = to
                if actionIN[2] == fr:
                    b = to
                if resultIN == fr:
                    resultIN = to
                t[l] = [(actionIN[0], a, b), resultIN]
            t.remove(t[i])
            i -= 1
        i += 1

    values = {}
    i = 0
    while i < len(t):
        action, result = t[i]
        if action[0] == "NUM":
            values[result] = int(action[1])
            t.remove(t[i])
            i -= 1
        i += 1
    values["EMPTY"] = 0
    values["1"] = 1
    return values

def decode(t: list[tuple[tuple[str, str, str], str]], values: dict[str, int]) -> int:
    """
    Processes the instructions by doing the ones where the wire values are known.

    Args:
        t: The list of instructions
        values: the dictionary containing some wires and their values
    
    Returns:
        The value of wire "a".
    """
    while "a" not in values.keys():
        i = 0
        while i < len(t):
            action, result = t[i]
            if action[1] in values:
                if action[0] == "NOT":
                    values[result] = 65535 - values[action[1]]
                    t.remove(t[i])
                    i -= 1
                elif action[0] == "AND" and action[2] in values:
                    values[result] = values[action[1]] & values[action[2]]
                    t.remove(t[i])
                    i -= 1
                elif action[0] == "OR" and action[2] in values:
                    values[result] = values[action[1]] | values[action[2]]
                    t.remove(t[i])
                    i -= 1
                elif action[0] == "LSHIFT":
                    values[result] = values[action[1]] << int(action[2])
                    t.remove(t[i])
                    i -= 1
                elif action[0] == "RSHIFT":
                    values[result] = values[action[1]] >> int(action[2])
                    t.remove(t[i])
                    i -= 1
            i += 1
    return values["a"]


if __name__ == "__main__":
    t = read_file()
    t2 = copy.deepcopy(t)
    values = remove_singles(t)
    print("Part 1:", decode(t, values))
    for i in t2:
        if i[1] == "b":
            t2.remove(i)
    t2.append((("NUM", 3176, "EMPTY"), "b"))
    values2 = remove_singles(t2)
    print("Part 2:", decode(t2, values2))