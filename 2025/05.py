def read_file() -> tuple[list[tuple[int, int]], list[int]]:
    """
    Reads the file and returns it as a tuple of lists.
    The intervals are stored as a list of tuple of integers, the beginnings and the ends of the intervals.
    The IDs are returned as a list of integers.

    Returns:
        The tuple of the two lists.
    """
    intervals = []
    ids = []
    on_id = False
    with open("2025/5.txt", "r") as f:
        for i in f:
            if i == "\n":
                on_id = True
                continue
            if on_id:
                ids.append(int(i.split("\n")[0]))
            else:
                a, b = i.split("\n")[0].split("-")
                intervals.append((int(a), int(b)))
    return intervals, ids

def check_fresh(intervals: list[tuple[int, int]], ids: list[int]) -> int:
    """
    Returns the number of IDs that are withing the intervals.

    Args:
        intervals: Tuples containing the beginnings and the ends of the intervals.
        ids: The IDs that are to be checked.

    Returns:
        The numbers of IDs within the intervals.
    """
    correct = 0
    for id in ids:
        for a, b in intervals:
            if id >= a and id <= b:
                correct += 1
                break
    return correct

def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merges the intervals, so that each interval covers a distinct set of numbers.

    Args:
        intervals: Tuples containing the beginnings and the ends of the intervals.
    
    Returns:
        A shorter list of distinct intervals.
    """
    old_size = len(intervals)
    intervals.sort()
    i = 0
    while i < len(intervals):
        j = i + 1
        while j < len(intervals):
            a, b = intervals[i]
            x, y = intervals[j]
            if b < x:
                break
            if a <= x and x <= y and y <= b: # a x y b
                intervals.remove(intervals[j])
                j -= 1
            elif x <= a and a <= b and b <= y: # x a b y
                intervals[i] = (x, y)
                intervals.remove(intervals[j])
                j -= 1
            elif a <= x and x <= b and b <= y: # a x b y
                intervals[i] = (a, y)
                intervals.remove(intervals[j])
                j -= 1
            elif x <= a and a <= y and y <= b: # x a y b
                intervals[i] = (x, b)
                intervals.remove(intervals[j])
                j -= 1
            j += 1
        i += 1
    return intervals

def intervals_size(intervals: list[tuple[int, int]]) -> int:
    """
    Calculates the total number of numbers within the intervals.

    Args:
        intervals: Tuples containing the beginnings and the ends of the intervals.

    Returns:
        The total number of numbers within the intervals.
    """
    total = 0
    for a, b in intervals:
        total += (b - a + 1)
    return total


if __name__ == "__main__":
    intervals, ids = read_file()
    fixed_intervals = merge_intervals(intervals)
    print("Part 1:", check_fresh(fixed_intervals, ids))

    print("Part 2:", intervals_size(fixed_intervals))