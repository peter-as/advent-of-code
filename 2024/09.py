from typing import Union

def read_file() -> tuple[list[chr], int, list[tuple[Union[chr,int], int]]]:
    """
    Reads a line of numbers, and turns it the storage it represents

    Returns:
        A tuple of a list of characters, representing the storage, the amount of files, 
        and a list of tuples representing the files and space on the storage
    """ 
    l = []
    last = 0
    list_of_batches = []
    with open("2024/9.txt","r") as f:
        index = 0
        is_file = True

        for i in f.read():
            i = int(i)

            if is_file == True:
                for k in range(i):
                    l.append(index)
                list_of_batches.append((index, i))
                last += i
                index += 1
                is_file = False
            else:
                for k in range(i):
                    l.append(".")
                is_file = True
                list_of_batches.append((".", i))
        
    return l, last, list_of_batches

def calculate_checksum(line: list[chr]) -> int:
    """
    Calculates the checksum of the list, by multiplying the number with its index and summing it

    Args:
        line: The list representing the storage
    
    Returns:
        The calculated checksum
    """
    checksum = 0
    for i in range(len(line)):
        if not line[i] == ".":
            checksum += i * int(line[i])
    return checksum

def move_files(line: list[chr], last: int) -> int:
    """
    Moves the numbers from the end of the list, to the first '.', then returns the checksum of the storage

    Args:
        line: The list representing the storage
        last: The index where the last file will end up at

    Returns:
        The checksum of the storage
    """
    num = 0
    last_index = 0
    for i in range(len(line) - 1, 0, -1):
        if not line[i] == ".":
            num = int(line[i])
            last_index = i
            break

    first_index = 0
    while last_index > last and first_index < last + 1:
        if line[first_index] == ".":
            while line[last_index] == ".":
                last_index -= 1
            line[first_index] = line[last_index]
            line[last_index] = "."
        first_index += 1
    return calculate_checksum(line)

def move_files_that_fit(list_of_batches: list[tuple[Union[chr,int], int]]):
    """
    Moves the whole batch of files at once from the end of the list to the first available space if possible

    Args:
        list_of_batches: A list of tuples representing the files and space on the storage

    Returns:
        The checksum of the storage
    """
    index = len(list_of_batches) - 1
    while index > 0:
        if list_of_batches[index][0] == ".":
            index -= 1
            continue

        # File found, start search from left side
        for left in range(index):
            if not list_of_batches[left][0] == ".":
                continue
            # If their size is equal swap them
            if list_of_batches[left][1] == list_of_batches[index][1]:
                list_of_batches[left] = list_of_batches[index]
                new_batch = (".",list_of_batches[index][1])
                list_of_batches[index] = new_batch
                break

            # If there is more free space than the size of the file
            elif list_of_batches[left][1] > list_of_batches[index][1]:
                new_batch = (".", list_of_batches[left][1] - list_of_batches[index][1])
                list_of_batches[left:left+1] = list_of_batches[index], new_batch
                index += 1
                if list_of_batches[left + 2][0] == ".":
                    list_of_batches[left + 1] = (".", list_of_batches[left+1][1] + list_of_batches[left + 2][1])
                    list_of_batches.pop(left + 2)
                    index -= 1
                
                new_batch = (".",list_of_batches[index][1])
                list_of_batches[index] = new_batch

                if (list_of_batches[index - 1][0] == "."):
                    list_of_batches[index - 1] = (".", list_of_batches[index - 1][1] + list_of_batches[index][1])
                    list_of_batches.pop(index)
                if (list_of_batches[index + 1][0] == "."):
                    list_of_batches[index] = (".", list_of_batches[index][1] + list_of_batches[index + 1][1])
                    list_of_batches.pop(index + 1)

                break
        index -= 1
        
    rebuilt_files = []
    for i in list_of_batches:
        for j in range(i[1]):
            rebuilt_files.append(i[0])
    return calculate_checksum(rebuilt_files)

if __name__ == "__main__":
    line, last, list_of_batches = read_file()
    print("Part 1:", move_files(line, last - 1))
    print("Part 2:", move_files_that_fit(list_of_batches))
