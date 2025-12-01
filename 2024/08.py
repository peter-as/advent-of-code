import math

def open_file() -> tuple[int, int, dict[chr, list[tuple[int, int]]]]:
    """
    Reads in the table, and stores the locations of the antenna

    Returns:
        A tuple of the height and width of the table, and a dictionary of the antennas and their indices
    """
    l = []
    d = {}
    with open("2024/8.txt") as f:
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

def antinodes_between_same_frequency(n: int, m: int, d: dict[chr, list[tuple[int, int]]], frequency: chr) -> set[tuple[int, int]]:
    """
    Takes every location of an antenna, and calculates where antinodes could go

    Args:
        n: the height of the table
        m: the width of the table
        d: a dictionary of the antennas and a list of their indeces in tuples
        frequency: the antenna being used

    Returns:
        A set of the tuple indices of the location of the antinodes
    """
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
            # I figure out in what relation to each other the two antennas are positioned on the table
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
            
            # Are the antinodes in the table?
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
                    
def find_antinodes(n: int, m: int, d: dict[chr, list[tuple[int, int]]], in_line = False) -> set[tuple[int, int]]:
    """
    Goes through every type of antennas, and finds locations for antinodes

    Args:
        n: the height of the table
        m: the width of the table
        d: a dictionary of the antennas and a list of their indeces in tuples
        in_line: True if the antinodes should be in the whole line, false if only aligned with the other antennas

    Returns:
        A set of the tuple indices of the locations of antinodes
    """
    indices = set()
    if not in_line:
        for i in d:
            indices = indices.union(antinodes_between_same_frequency(n, m, d, i))
    else:
        for i in d:
            indices = indices.union(antinodes_in_same_row(n, m, d, i))
    return indices

def antinodes_in_same_row(n: int, m: int, d: dict[chr, list[tuple[int,int]]], frequency: chr) -> set[tuple[int, int]]:
    """
    Takes every location of an antenna, and calculates where antinodes could go in the same line as the antennas

    Args:
        n: the height of the table
        m: the width of the table
        d: a dictionary of the antennas and a list of their indeces in tuples
        frequency: the antenna being used

    Returns:
        A set of the tuple indices of the location of the antinodes
    """
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
            # I figure out in what relation to each other the two antennas are positioned on the table
            if (i1 > i2 and j1 > j2) or (i1 < i2 and j1 < j2):
                dr = True
            indices.add((i1,j1))
            
            # Are the antinodes in the table?
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

if __name__ == "__main__":
    n, m, d = open_file()
    print("Part 1:",len(find_antinodes(n, m, d)))
    print("Part 2:",len(find_antinodes(n, m, d, in_line = True)))
