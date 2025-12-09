def read_file() -> list[tuple[int, int, int]]:
    """
    Reads the file and stores the coordinates of each box.

    Returns:
        The list of coordinates.
    """
    coordinates = []
    with open("2025/8.txt", "r") as f:
        for i in f:
            l = i.split(",")
            coordinates.append((int(l[0]), int(l[1]), int(l[2])))
    return coordinates

def build_groups(coordinates: list[tuple[int, int, int]]) -> tuple[list[tuple[int, int, int]], list[set[int]], list[int]]:
    """
    Using the coordinates builds a list of distances, and other lists that show how the boxes are connected

    Args:
        coordinates: The list containing the coordinates of the boxes.

    Returns:
        A list containing tuples of the distance between two boxes, and their indices, sorted in increasing order.
        A list of sets, where each set represents a grouping of boxes.
        A list of integers, where x value at index i means box i is in group x.
    """
    distances = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            a, b, c = coordinates[i]
            x, y, z = coordinates[j]
            distances.append(((a - x) ** 2 + (b - y) ** 2 + (c - z) ** 2, i, j))
    distances.sort()
    connections = [set([i]) for i in range(len(coordinates))]
    locations = [i for i in range(len(coordinates))]
    return distances, connections, locations

def connect_boxes(distances: list[tuple[int, int, int]], connections: list[set[int]], locations: list[int]) -> int:
    """
    Connects the boxes based on edges in distances, and returns the product of the size of the biggest groups.

    Args:
        distances: A list containing tuples of the distance between two boxes, and their indices, sorted in increasing order.
        connections: A list of sets, where each set represents a grouping of boxes.
        locations: A list of integers, where x value at index i means box i is in group x.

    Returns: The product of the size of the 3 biggest group of boxes.

    """
    for i in range(len(distances)):
        x, y = distances[i][1:]
        setx = locations[x]
        sety = locations[y]
        if setx != sety:
            for f in connections[sety]:
                locations[f] = setx
            connections[setx] = connections[setx].union(connections[sety])
            connections[sety] = {}
    lengths = [len(x) for x in connections]
    lengths.sort(reverse = True)
    return(lengths[0] * lengths[1] * lengths[2])

def last_x(distances: list[tuple[int, int, int]], coordinates: list[tuple[int, int, int]], connections: list[set[int]], locations: list[int]) -> int:
    """
    Connects the boxes based on edges in distance until they are in a single group, 
    and returns the product of the X coordinates of the two boxes that make the last connection.

    Args:
        distances: A list containing tuples of the distance between two boxes, and their indices, sorted in increasing order.
        coordinates: The list containing the coordinates of the boxes.
        connections: A list of sets, where each set represents a grouping of boxes.
        locations: A list of integers, where x value at index i means box i is in group x.

    Returns: The product of the size of the 3 biggest group of boxes.
    """
    x_1 = 0
    x_2 = 1
    boxes = len(connections) - connections.count({})
    i = 0
    while boxes > 1:
        x, y = distances[i][1:]
        setx = locations[x]
        sety = locations[y]
        if setx != sety:
            for f in connections[sety]:
                locations[f] = setx
            connections[setx] = connections[setx].union(connections[sety])
            connections[sety] = {}
            x_1 = coordinates[x][0]
            x_2 = coordinates[y][0]
            boxes -= 1
        i += 1
    return(x_1 * x_2)


if __name__ == "__main__":
    coordinates = read_file()
    distances, connections, locations = build_groups(coordinates)
    n = 1000
    print("Part 1:", connect_boxes(distances[:n], connections, locations))
    print("Part 2:", last_x(distances[n:], coordinates, connections, locations))