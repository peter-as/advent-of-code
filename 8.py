import math

def open_file():
    f = open("8.txt")
    l = []
    d = {}
    index = -1
    for i in f:
        index += 1
        i = i.split("\n")[0]
        l.append(i)
        for j in range(len(i)):
            if not i[j] == ".":
                if i[j] not in d:
                    d[i[j]] = [(index,j)]
                else:
                    d[i[j]].append((index,j))
    return len(l), len(l[0]), d

def antinodes_between_same_frequency(n,m,d,frequency):
    indices = set()
    for node_index in range(len(d[frequency])):
        for other_node in range(node_index + 1, len(d[frequency])):
            i1,j1 = d[frequency][node_index][0], d[frequency][node_index][1]
            i2,j2 = d[frequency][other_node][0], d[frequency][other_node][1]
            i_difference = abs(i1 - i2)
            j_difference = abs(j1 - j2)
            dr = False
            l = [(i1,j1),(i2,j2)]
            f, s = 0,0
            if i1 > i2 and j1 > j2:
                dr = True
                f, s = 1, 0
            elif i1 < i2 and j1 < j2:
                dr = True
                f, s = 0, 1
            elif i1 < i2 and j2 < j1:
                f, s = 1, 0
            else:
                f, s = 0, 1
            if dr:
                i3,j3 = l[s][0]+i_difference, l[s][1]+j_difference
                if i3 < n and j3 < m:
                    indices.add((i3,j3))
                i3,j3 = l[f][0]-i_difference, l[f][1]-j_difference
                if i3 >= 0 and j3 >= 0:
                    indices.add((i3,j3))
            else:
                i3,j3 = l[s][0]-i_difference, l[s][1]+j_difference
                if i3 >= 0 and j3 < m:
                    indices.add((i3,j3))
                i3,j3 = l[f][0]+i_difference, l[f][1]-j_difference
                if i3 < n and j3 >= 0:
                    indices.add((i3,j3))
    return indices
                
            
    

def find_antinodes(n,m,d):
    indices = set()
    for i in d:
        indices = indices.union(antinodes_between_same_frequency(n,m,d,i))

    return indices


def antinodes_in_same_row(n,m,d,frequency):
    indices = set()
    for node_index in range(len(d[frequency])):
        for other_node in range(node_index + 1, len(d[frequency])):
            i1,j1 = d[frequency][node_index][0], d[frequency][node_index][1]
            i2,j2 = d[frequency][other_node][0], d[frequency][other_node][1]
            i_difference = abs(i1 - i2)
            j_difference = abs(j1 - j2)
            gcd = math.gcd(i_difference, j_difference)
            i_difference //= gcd
            j_difference //= gcd
            dr = False
            f, s = 0,0
            if (i1 > i2 and j1 > j2) or (i1 < i2 and j1 < j2):
                dr = True
            indices.add((i1,j1))
            if dr:
                i3,j3 = i1 + i_difference, j1 + j_difference
                while i3 < n and j3 < m:
                    indices.add((i3,j3))
                    i3 += i_difference
                    j3 += j_difference

                i3,j3 = i1 - i_difference, j1 - j_difference
                while i3 >= 0 and j3 >= 0:
                    indices.add((i3,j3))
                    i3 -= i_difference
                    j3 -= j_difference
                    
            else:
                i3,j3 = i1 - i_difference, j1 + j_difference
                while i3 >= 0 and j3 < m:
                    indices.add((i3,j3))
                    i3 -= i_difference
                    j3 += j_difference

                i3,j3 = i1 + i_difference, j1 - j_difference
                while i3 < n and j3 >= 0:
                    indices.add((i3,j3)) 
                    i3 += i_difference
                    j3 -= j_difference
    return indices
                


def find_full_row_antinodes(n,m,d):
    indices = set()
    for i in d:
        indices = indices.union(antinodes_in_same_row(n,m,d,i))

    return indices

n,m,d = open_file()
print("Part 1:",len(find_antinodes(n,m,d)))
print("Part 2:",len(find_full_row_antinodes(n,m,d)))
