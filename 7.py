def read_file():
    f = open("7.txt","r")
    l = []
    for i in f:
        k = i.split(":")
        k[0] = int(k[0])
        k[1] = [int(x) for x in k[1].split()]
        l.append(k)
    return l

def add_operators(final_sum,elements,part_sum, expanded = False):
    if len(elements) == 0:
        if final_sum == part_sum:
            return True
        return False
    if len(elements) == 1:
        if add_operators(final_sum,[],part_sum + elements[0], expanded):
            return True
        if add_operators(final_sum,[],part_sum * elements[0], expanded):
            return True
        if expanded:
            if add_operators(final_sum,[],int(str(part_sum) + str(elements[0])),expanded):
                return True
        return False
    
    if add_operators(final_sum,elements[1:],part_sum + elements[0],expanded):
        return True
    if add_operators(final_sum,elements[1:],part_sum * elements[0],expanded):
        return True
    if expanded:
        if add_operators(final_sum,elements[1:],int(str(part_sum) + str(elements[0])),expanded):
            return True
    return False


def check_if_sum_can_be_achieved(list,expanded = False):
    sum = 0
    for i in list:
        if add_operators(i[0],i[1][1:],i[1][0], expanded):
            sum += i[0]
    return sum

l = read_file()
print("Part 1:",check_if_sum_can_be_achieved(l))
print("Part 2:",check_if_sum_can_be_achieved(l, True))
