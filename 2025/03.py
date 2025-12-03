def read_file() -> list[list[int]]:
    """
    Reads the file and returns it as a list of list of integers.
    Each row is a different list, where every character in the row is an integer in the list

    Returns:
        The list of list of integers.
    """
    t = []
    with open("2025/3.txt", "r") as f:
        for i in f:
            l = []
            for n in i.split("\n")[0]:
                l.append(int(n))
            t.append(l)
    return t

def highest_joltage(t: list[list[int]], num_battery: int) -> int:
    """
    Finds the highest number constructable from the numbers in a row. Each number has to have i < j index in the original list
    
    Args:
        t: The row of numbers
        num_battery: the number of digits that have to be picked from each row

    Returns:
        The sum of the constructed numbers in each row
    """
    total = 0
    for bank in t:
        batteries = [0] * num_battery
        indices = [0] * num_battery
        for b in range(num_battery):
            i = indices[b]
            while i < len(bank) - num_battery + b + 1:
                if bank[i] > batteries[b]:
                    batteries[b:] = bank[i : i + num_battery - b]
                    indices[b:] = [x for x in range(i, i + num_battery - b)]
                i += 1
        jolt = 0
        for i in range(num_battery):
            jolt += (10 ** i) * batteries[-i - 1]
        total += jolt
    return total


if __name__ == "__main__":
    t = read_file()
    print("Part 1:", highest_joltage(t, 2))
    print("Part 2:", highest_joltage(t, 12))