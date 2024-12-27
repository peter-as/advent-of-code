def read_file():
    f = open("10.txt","r")
    l = []
    zeros = []
    index = 0
    for i in f:
        i = i.split("\n")[0]
        for j in range(len(i)):
            if i[j] == "0":
                zeros.append((index+1,int(j)+1))
        l.append("."+i+".")
        index += 1
    k = len(l[0])
    l.insert(0,k*".")
    l.append(k*".")
    return l, zeros

def check_all_neighbours(table, i , j):
    if table[i][j] == "9":
        return 1
    total = 0
    if not table[i-1][j] == "." and int(table[i-1][j]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i-1, j)
    if not table[i+1][j] == "." and int(table[i+1][j]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i+1, j)
    if not table[i][j-1] == "." and int(table[i][j-1]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i, j-1)
    if not table[i][j+1] == "." and int(table[i][j+1]) == int(table[i][j])+1:
        total += check_all_neighbours(table, i, j+1)
    return total

def check_reachable_ends(table, i , j):
    if table[i][j] == "9":
        k = set()
        k.add((i,j))
        return k
    k = set()
    if not table[i-1][j] == "." and int(table[i-1][j]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i-1, j))
    if not table[i+1][j] == "." and int(table[i+1][j]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i+1, j))
    if not table[i][j-1] == "." and int(table[i][j-1]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i, j-1))
    if not table[i][j+1] == "." and int(table[i][j+1]) == int(table[i][j])+1:
        k = k.union(check_reachable_ends(table, i, j+1))
    return k


def reachable_ends(table, zeros):
    trails = 0
    for i in zeros:
        found = check_reachable_ends(table, i[0], i[1])
        trails += len(found)
    return trails   

def count_trails(table, zeros):
    trails = 0
    for i in zeros:
        found = check_all_neighbours(table, i[0], i[1])
        #print(i,found)
        trails += found
    return trails        
    

table, zeros = read_file()
print("Part 1:", reachable_ends(table, zeros))
print("Part 2:", count_trails(table,zeros))
