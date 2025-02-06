def read_file():
    # I read the file and 
    f = open("2024/9.txt","r")
    # index keeps track of the number to use, step is if we have empty space or numbers, last keeps track how many characters -1 we have
    # l contains a character for every spot, list_of_batches keeps track of how many of what characters we have in a batch
    l = []
    index = 0
    step = 0
    last = -1
    list_of_batches = []
    for i in f.read():
        i = int(i)
        # If step is 0 we have numbers
        if step == 0:
            for k in range(i):
                l.append(index)
            list_of_batches.append((index,i))
            last += i
            index += 1
            step = 1
        # If step is 1 we have empty space
        else:
            for k in range(i):
                l.append(".")
            step = 0
            list_of_batches.append((".",i))
    
    return l, last, list_of_batches

def calculate_checksum(line):
    # We calculate the checksum on the line by looping over it and adding the number * index to a sum
    checksum = 0
    for i in range(len(line)):
        if not line[i] == ".":
            checksum += i * int(line[i])
    return checksum

def move_files(line, last):
    num = 0
    last_index = 0
    # We find where the last number is in the list
    for i in range(len(line)-1,0,-1):
        if not line[i] == ".":
            num = int(line[i])
            last_index = i
            break
    first_index = 0
    # We progress backwards through the list, and try to move things to the beginning
    # We do this until our back index reaches the number of numbers we have, since we are done after that
    while last_index > last and first_index < last + 1:
        # If we have an available spot, we progress backwards until we get to a number, and move it there
        if line[first_index] == ".":
            while line[last_index] == ".":
                last_index -= 1
            line[first_index] = line[last_index]
            line[last_index] = "."
        first_index += 1
    return calculate_checksum(line)

def move_files_that_fit(list_of_batches):
    # Start at the end of the list and go backwards. If we find a file start from the left side and see if there is a space where it fits
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
                # Create a new batch of empty space based on how much is left after moving
                new_batch = (".", list_of_batches[left][1] - list_of_batches[index][1])
                # We move the file and add the remaining space
                list_of_batches[left:left+1] = list_of_batches[index], new_batch
                index += 1
                # If the next batch is empty space we merge
                if list_of_batches[left + 2][0] == ".":
                    list_of_batches[left + 1] = (".", list_of_batches[left+1][1] + list_of_batches[left + 2][1])
                    list_of_batches.pop(left + 2)
                    index -= 1
                
                new_batch = (".",list_of_batches[index][1])
                list_of_batches[index] = new_batch
                # Check if there is empty space before and after where the file was, then merge
                if (list_of_batches[index - 1][0] == "."):
                    list_of_batches[index - 1] = (".", list_of_batches[index - 1][1] + list_of_batches[index][1])
                    list_of_batches.pop(index)
                if (list_of_batches[index + 1][0] == "."):
                    list_of_batches[index] = (".", list_of_batches[index][1] + list_of_batches[index + 1][1])
                    list_of_batches.pop(index + 1)

                break
        index -= 1
    # Rebuild the row from the batches, one character per element
    rebuilt_files = []
    for i in list_of_batches:
        for j in range(i[1]):
            rebuilt_files.append(i[0])
    return calculate_checksum(rebuilt_files)

line, last, list_of_batches = read_file()
print("Part 1:",move_files(line, last))
print("Part 2:", move_files_that_fit(list_of_batches))
