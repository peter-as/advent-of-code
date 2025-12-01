def read_input() -> tuple[list[tuple[int]], list[list[int]]]:
    """
    Reads in the input into two lists, the first half as a list of tuples of int, the second half as list of list of ints

    Returns:
        A tuple of a list of tuples of ints, and a list of list of ints
    """

    connections = []
    prints = []
    with open("2024/5.txt","r") as f:
        step = 0
        for i in f:
            if i == "\n":
                step = 1
                continue
            if step == 0:
                l = i.split("|")
                connections.append((int(l[0]),int(l[1])))
            else:
                l = i.split()[0].split(",")
                for j in range(len(l)):
                    l[j] = int(l[j])
                prints.append(l)
    return connections, prints

def build_graph(connections: list[tuple[int]]) -> dict[int, int]:
    """
    Builds a dictionary out of the connections between the tuples of the list

    Args:
        connections: The list of tuples of connected vertices
    
    Returns:
        A dictionary showing the connections between vertices
    """
    incoming = {}
    for i in connections:
        x, y = i[0], i[1]
        if y not in incoming:
            incoming[y] = [x]
        else:
            incoming[y].append(x)
    return incoming

def in_order(graph: dict[int, int], prints: list[list[int]]) -> int:
    """
    Checks which prints can be printed, and returns the sum of the middle elements
    Checks if any of the future pages are a requisite of the current print, if yes that is incorrect

    Args:
        graph: The dictionary showing the connections between vertices
        prints: the list of page numbers in which order they should be printed

    Returns:
        The sum of the middle elements of the possible prints
    """

    middle = 0
    for l in prints: # I check all the prints
        success = True
        for i in range(len(l)):
            upcoming = l[i+1:]

            if l[i] in graph and len(list(set(graph[l[i]]).intersection(set(upcoming)))) > 0:
                # If anything that would need to be completed first would appear later, this is impossible
                success = False
                break
        if success:
            middle += l[len(l)//2]
    return middle

def put_in_order(graph: dict[int, int], prints: list[list[int]]) -> int:
    """
    Puts the prints in order, then sums the middle elements

    Args:
        graph: The dictionary showing the connections between vertices
        prints: the list of page numbers in which order they should be printed

    Returns:
        The sum of the middle elements of the possible prints
    """
    middle = 0
    for l in prints:
        for i in range(len(l)):
            upcoming = l[i+1:]
            if l[i] in graph and len(list(set(graph[l[i]]).intersection(set(upcoming)))) > 0:
                # If anything that would need to be completed first would appear later, this is impossible, I need to put it in order
                
                remain = l[i:] # I need to keep track of what I have not sorted yet
                j = i
                while j <= len(l)//2:
                    for left in range(0,len(l)-j):
                        # I go through the remaining updates, and and if there is something else that needs to be completed first, 
                        # this cannot be the next, skip
                        if not len(list(set(graph[remain[left]]).intersection(set(remain) - {remain[left]}))) == 0:
                            continue

                        l[j] = remain[left]
                        remain.remove(remain[left])
                        break
                    j += 1
                break
        middle += l[len(l)//2]
    return middle        

if __name__ == "__main__":
    connections, prints = read_input()
    graph = build_graph(connections)

    successful = in_order(graph, prints)
    print("Part 1:", successful)
    print("Part 2:", put_in_order(graph, prints) - successful)
