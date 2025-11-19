def read_file() -> list[tuple[int, list[int]]]:
    """
    Reads in the rows of numbers as tuples of the first number, and a list of the list of numbers

    Returns:
        The list of the tuples, where the first half of the tuple is the number, and the second is the list of numbers
    """
    l = []
    with open("2024/7.txt","r") as f:
        for i in f:
            k = i.split(":")
            k[0] = int(k[0])
            k[1] = [int(x) for x in k[1].split()]
            l.append((k[0], k[1]))
    return l

def add_operators(final_sum: int, elements: list[int], part_sum: int, concat = False):
    """
    Recursively adds operators to see if they would amount to the correct sum

    Args:
        final_sum: the required final value
        elements: the remaining numbers still to be added
        part_sum: the value so far
        concat: can concatenation be used

    Returns:
        Boolean value showing if the required value was achieved

    """
    if len(elements) == 0 or part_sum > final_sum:
        if final_sum == part_sum:
            return True
        return False
    
    if add_operators(final_sum,elements[1:], part_sum + elements[0], concat): # +
        return True
    if add_operators(final_sum,elements[1:], part_sum * elements[0], concat): # *
        return True
    if concat:
        if add_operators(final_sum,elements[1:], int(str(part_sum) + str(elements[0])), concat):
            return True
    return False


def can_sum_be_achieved(list: list[tuple[int, list[int]]], concat = False):
    """
    Checks if the first element of the tuples can be made out of the numbers in the second half
    Sums the possible values

    Args:
        list: the tuples of numbers and list of numbers
        concat: can concat be used as an operator
    
    Returns:
        The sum of possible numbers
    """
    sum = 0
    for i in list:
        if add_operators(i[0],i[1][1:],i[1][0], concat):
            sum += i[0]
    return sum

if __name__ == "__main__":
    l = read_file()
    print("Part 1:",can_sum_be_achieved(l))
    print("Part 2:",can_sum_be_achieved(l, concat = True))