def read_file() -> list[str]:
    """
    Reads the list of words from a file and stores them in a list

    Returns:
        The list of strings
    """
    l = []
    with open("2015/5.txt", "r") as f:
        for i in f:
            l.append(i)
    return l

def nice_string(words: list[str]) -> int:
    """
    Looks for nice words that fulfill the 3 rules of not having specific substrings, having at least 3 vowels and having double letters

    Args:
        words: The list of words

    Returns:
        The number of nice words
    """
    total = 0
    for i in words:
        if "ab" in i or "cd" in i or "pq" in i or "xy" in i:
            continue
        if i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u') < 3:
            continue
        if True in [True if c * 2 in i else False for c in list(map(chr, range(97, 123)))]:
            total += 1
    return total

def new_rules(words: list[str]) -> int:
    """
    Looks for nice words that fulfill 2 new rules of not having 2 same characters with another in between,
    and having a pair of consecutive characters appearing at least twice seperately in the string

    Args:
        words: The list of words

    Returns:
        The number of nice words
    """
    total = 0
    for i in words:
        doub = False
        between = False
        for letter in range(len(i) - 2):
            if i[letter] + i[letter + 1] in i[letter + 2:]:
                doub = True
            if i[letter] == i[letter + 2]:
                between = True
        if doub and between:
            total += 1
    return total


if __name__ == "__main__":
    words = read_file()
    print("Part 1:", nice_string(words))
    print("Part 2:", new_rules(words))
