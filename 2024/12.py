def read_file() -> list[str]:
    """
    Reads in the map from the file and stores it as a list of strings

    Returns:
        A list of strings representing the map
    """
    t = []
    with open("2024/12.txt","r") as f:
        for i in f:
            i = i.split("\n")[0]
            t.append("*" + i + "*")
        pad = (len(t) + 2) * "*"
        t.insert(0,pad)
        t.append(pad)
    return t

def discover_field(field: list[str], i: int, j: int, visited: set[tuple[int, int]]) -> tuple[int, int, set[tuple[int, int]],
                                                                                            set[tuple[int, int]], 
                                                                                            set[tuple[int, int]], 
                                                                                            set[tuple[int, int]], 
                                                                                            set[tuple[int, int]]]:
    """
    Recursiely explores the map to find the whole garden it is currently located in

    Args:
        field: A list of strings representing the maps
        i: The current x coordinate
        j: The current y coordinate
        visited: A set of the visited coordinates as a tuple of integers

    Returns:
        A tuple of the size of the visited area, number of edges, every visited coordinates,
        and sets containing the coordinates of the edges, 
        split up based on if they are on the top, left, right, or bottom side of the garden
    """
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

def count_sides(up: set[tuple[int, int]], down: set[tuple[int, int]], left: set[tuple[int, int]], right: set[tuple[int, int]]) -> int:
    """
    Given sets of tuples of coordinates containing the respective borders of the garden, counts how many seperate sides it has
    
    Args:
        up: A set of tuple of integers, containing the upper border edges of the garden
        down: A set of tuple of integers, containing the bottom border edges of the garden
        left: A set of tuple of integers, containing the left border edges of the garden
        right: A set of tuple of integers, containing the right border edges of the garden

    Returns:
        The number of seperate sides of the garden
    """
    sides = 0
    while len(list(up)) > 0:
        up = up.difference(count(up, list(up)[0], '-', set()))
        sides += 1
        
    while len(list(down)) > 0:
        down = down.difference(count(down, list(down)[0], '-', set()))
        sides += 1

    while len(list(left)) > 0:
        left = left.difference(count(left, list(left)[0], '|', set()))
        sides += 1

    while len(list(right)) > 0:
        right = right.difference(count(right, list(right)[0], '|', set()))
        sides += 1

    return sides

def count(side: set[tuple[int, int]], current: tuple[int, int], direction: chr, visited: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Traverses a set of edges all facing the same side from one edge, to find every edge that are part of the starting edge's border

    Args:
        side: A set of edges all on the same side of the garden
        current: The current edge
        direction: The direction the edge is laid - '-' or '|'
        visited: the set of tuples of coordinates of the visited edges
    
    Returns:
        The set of visited edges
    """
    visited.add(current)
    i, j = current[0], current[1]
    if direction == '-':
        if (i, j-1) not in visited and (i, j-1) in side:
            visited.add((i, j-1))
            visited.union(count(side, (i, j-1), '-', visited))
        if (i, j+1) not in visited and (i, j+1) in side:
            visited.add((i, j+1))
            visited.union(count(side, (i, j+1), '-', visited))
    else:
        if (i-1, j) not in visited and (i-1, j) in side:
            visited.add((i-1, j))
            visited.union(count(side, (i-1, j), '|', visited))
        if (i+1, j) not in visited and (i+1, j) in side:
            visited.add((i+1, j))
            visited.union(count(side, (i+1, j), '|', visited))
    return visited

def find_fields(field: list[str]) -> tuple[int, int]:
    """
    Given a list of strings, represing the map, provides the cost of fencing, when using the perimeter, or when using the number of sides

    Args: 
        field: A list of strings representing the map

    Returns:
        A tuple containing the two prices of the fence, based on if using the perimeter, or using the number of sides
    """
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

if __name__ == "__main__":
    field = read_file()
    total_1, total_2 = find_fields(field)
    print("Part 1:", total_1)
    print("Part 2:", total_2)