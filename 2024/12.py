def read_file():
    f = open("12.txt","r")
    t = []
    for i in f:
        i = i.split("\n")[0]
        t.append("*" + i + "*")
    pad = (len(t) + 2) * "*"
    t.insert(0,pad)
    t.append(pad)
    return t

def discover_field(field, i, j, visited):
    new_visited = visited.union({(i, j)})
    area, region = 1,0
    up, down, left, right = set(), set(), set(), set()

    #UP
    if field[i - 1][j] == field[i][j]:
        if (i - 1, j) not in new_visited:
            area_new, region_new, visited_new, up_n, down_n, left_n, right_n = discover_field(field, i-1, j, new_visited )
            area += area_new
            region += region_new
            new_visited = new_visited.union(visited_new)
            up = up.union(up_n)
            down = down.union(down_n)
            left = left.union(left_n)
            right = right.union(right_n)
    else:
        region += 1
        up.add((i, j))

    #DOWN
    if field[i + 1][j] == field[i][j]:
        if (i + 1, j) not in new_visited:
            area_new, region_new, visited_new, up_n, down_n, left_n, right_n = discover_field(field, i+1, j, new_visited )
            area += area_new
            region += region_new
            new_visited = new_visited.union(visited_new)
            up = up.union(up_n)
            down = down.union(down_n)
            left = left.union(left_n)
            right = right.union(right_n)
    else:
        region += 1
        down.add((i, j))

    #LEFT
    if field[i][j - 1] == field[i][j]:
        if (i, j -1) not in new_visited:
            area_new, region_new, visited_new, up_n, down_n, left_n, right_n = discover_field(field, i, j - 1, new_visited )
            area += area_new
            region += region_new
            new_visited = new_visited.union(visited_new)
            up = up.union(up_n)
            down = down.union(down_n)
            left = left.union(left_n)
            right = right.union(right_n)
    else:
        region += 1
        left.add((i, j))

    #RIGHT
    if field[i][j + 1] == field[i][j]:
        if (i, j + 1) not in new_visited:
            area_new, region_new, visited_new, up_n, down_n, left_n, right_n = discover_field(field, i, j + 1, new_visited )
            area += area_new
            region += region_new
            new_visited = new_visited.union(visited_new)
            up = up.union(up_n)
            down = down.union(down_n)
            left = left.union(left_n)
            right = right.union(right_n)
    else:
        region += 1
        right.add((i, j))

    return area, region, new_visited, up, down, left, right

def count_sides(up, down, left, right):
    sides = 0
    while len(list(up)) > 0:
        up = up.difference(count(up, list(up)[0], "S", set()))
        sides += 1
        
    while len(list(down)) > 0:
        down = down.difference(count(down, list(down)[0], "S", set()))
        sides += 1

    while len(list(left)) > 0:
        left = left.difference(count(left, list(left)[0], "H", set()))
        sides += 1

    while len(list(right)) > 0:
        right = right.difference(count(right, list(right)[0], "H", set()))
        sides += 1

    return sides


def count(side, current, direction, visited):
    visited.add(current)
    i, j = current[0], current[1]
    if direction == "S":
        if (i, j-1) not in visited and (i, j-1) in side:
            visited.add((i, j-1))
            visited.union(count(side, (i, j-1), "S", visited))
        if (i, j+1) not in visited and (i, j+1) in side:
            visited.add((i, j+1))
            visited.union(count(side, (i, j+1), "S", visited))
    else:
        if (i-1, j) not in visited and (i-1, j) in side:
            visited.add((i-1, j))
            visited.union(count(side, (i-1, j), "H", visited))
        if (i+1, j) not in visited and (i+1, j) in side:
            visited.add((i+1, j))
            visited.union(count(side, (i+1, j), "H", visited))
    return visited
        
            
        

def find_fields(field):
    visited = set()
    total = 0
    total_2 = 0
    for base_i in range(1, len(field) - 1):
        for base_j in range(1, len(field[base_i]) - 1):
            if (base_i, base_j) in visited:
                continue
            area, region, new_included, up, down, left, right = discover_field(field, base_i, base_j, visited)
            visited = visited.union(new_included)
            sides = count_sides(up, down, left, right)
            total += area * region
            total_2 += area * sides
    return total, total_2



field = read_file()
total_1, total_2 = find_fields(field)
print("Part 1:",total_1)
print("Part 2:",total_2)
