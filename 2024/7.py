def read_file():
    # I read the rows from the input. I store them as tuples, where the first element is the result, and the second are the nubmers
    f = open("2024/7.txt","r")
    l = []
    for i in f:
        k = i.split(":")
        k[0] = int(k[0])
        k[1] = [int(x) for x in k[1].split()]
        l.append(k)
    return l

def add_operators(final_sum,elements,part_sum, expanded = False):
    # I add operators recursively

    if len(elements) == 0:
        # If there are no more numbers left, I check if my result is the desired one
        if final_sum == part_sum:
            return True
        return False
    
    if add_operators(final_sum,elements[1:],part_sum + elements[0],expanded): # I check if I use addition here do I get the result
        return True
    if add_operators(final_sum,elements[1:],part_sum * elements[0],expanded): # I check if I use multiplication here do I get the result
        return True
    if expanded: # If I can use concatenation, I check if using it here would yield me the result
        if add_operators(final_sum,elements[1:],int(str(part_sum) + str(elements[0])),expanded):
            return True
    return False


def check_if_sum_can_be_achieved(list, expanded = False): # If expanded is true, it means I can also use concatenation
    sum = 0 # The final sum
    for i in list:
        if add_operators(i[0],i[1][1:],i[1][0], expanded):
            sum += i[0]
    return sum

l = read_file()
print("Part 1:",check_if_sum_can_be_achieved(l))
print("Part 2:",check_if_sum_can_be_achieved(l, True))
