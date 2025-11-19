from collections import defaultdict

def read_file() -> defaultdict[int, int]:
    """
    Reads a row of numbers from a file, and stores them in a default dict as keys, with 1 as value, representing the amount of stones

    Returns:
        A defaultdict showing the amount of a stone
    """
    with open("2024/11.txt","r") as f:
        line = [int(x) for x in f.read().split()]
        d = defaultdict(int)
        for i in line:
            d[i] += 1
        return d


def transform_stones(rocks: defaultdict[int, int], times: int) -> int:
    """
    Transforms the stones as 'times' amount of times

    Args:
        rocks: A defaultdict showing the amount of a stone
        times: the amount of times the stones get transformed

    Returns:
        The amount of stones after the transformations
    """
    for blink in range(times):
        change = defaultdict(int)
        for i in rocks:
            change[i] -= rocks[i]
            if i == 0:
                change[1] += rocks[i]
            elif len(str(i)) % 2 == 0:
                divider = int(10 ** (len(str(i))/2))
                f,s = i // divider, i % divider
                change[f] += rocks[i]
                change[s] += rocks[i]
            else:
                change[i * 2024] += rocks[i]
        for i in change:
            rocks[i] += change[i]
    sum = 0
    for i in rocks:
        sum += rocks[i]
    return sum
    
if __name__ == "__main__":
    rocks = read_file()
    print("Part 1:", transform_stones(rocks,25))
    rocks = read_file()
    print("Part 2:", transform_stones(rocks,75))
