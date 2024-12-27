def read_file():
    f = open("9.txt","r")
    l = []
    index = 0
    step = 0
    last = -1

    list_of_batches = []
    for i in f.read():
        i = int(i)
        if step == 0:
            for k in range(i):
                l.append(index)
            list_of_batches.append((index,i))
            last += i
            index += 1
            step = 1
        else:
            for k in range(i):
                l.append(".")
            step = 0
            list_of_batches.append((".",i))
    
    return l, last, list_of_batches

def calculate_checksum(line):
    checksum = 0
    for i in range(len(line)):
        if not line[i] == ".":
            checksum += i * int(line[i])
    return checksum

def move_files(line, last):
    num = 0
    last_index = 0
    for i in range(len(line)-1,0,-1):
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


def move_files_that_fit(list_of_batches):
    index = len(list_of_batches) - 1
    while index > 0:
        if list_of_batches[index][0] == ".":
            index -= 1
            continue
        for left in range(index):
            if not list_of_batches[left][0] == ".":
                continue
            if list_of_batches[left][1] == list_of_batches[index][1]:
                list_of_batches[left] = list_of_batches[index]
                new_batch = (".",list_of_batches[index][1])
                list_of_batches[index] = new_batch
                break
            elif list_of_batches[left][1] > list_of_batches[index][1]:
                new_batch = (list_of_batches[left][0], list_of_batches[left][1] - list_of_batches[index][1])
                list_of_batches[left:left+1] = list_of_batches[index], new_batch
                index += 1
                new_batch = (".",list_of_batches[index][1])
                list_of_batches[index] = new_batch
                break
        index -= 1
        i = 1
        while i < len(list_of_batches):
            if list_of_batches[i][0] == list_of_batches[i-1][0]:
                list_of_batches[i-1] = (list_of_batches[i-1][0],list_of_batches[i-1][1] + list_of_batches[i][1])
                list_of_batches.pop(i)
                i -= 1
            i += 1
        
    rebuilt_files = []
    for i in list_of_batches:
        for j in range(i[1]):
            rebuilt_files.append(i[0])
    return calculate_checksum(rebuilt_files)
    
    

line, last, list_of_batches = read_file()
print("Part 1:",move_files(line, last))
print("Part 2:", move_files_that_fit(list_of_batches))
