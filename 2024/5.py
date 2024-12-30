import copy

def read_input():
    # Read all the values from the input. I store them in two lists.
    # prints contains the prints I would like to do
    # connections has the pair of numbers that are connected

    f = open("2024/5.txt","r")
    connections = []
    prints = []
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
    return connections,prints

def build_graph(connections):
    # I create a dictionary, where I store all the connections in a graph-like manner
    # A vertex points to other vertices that needs to be completed first
    
    incoming = {}
    for i in connections:
        x, y = i[0], i[1]
        if y not in incoming:
            incoming[y] = [x]
        else:
            incoming[y].append(x)
    return incoming

def in_order(graph, prints):
    # I check if the requests are coming in order

    middle = 0
    for l in prints: # I check all the prints
        success = True
        for i in range(len(l)): # I go through the updates
            upcoming = l[i+1:] # I save a list of all the future updates
            if l[i] in graph and len(list(set(graph[l[i]]).intersection(set(upcoming)))) > 0:
                # If anything that would need to be completed first would appear later, this is impossible
                success = False
                break
        if success: # If possible, I add the middle element
            middle += l[len(l)//2]
    return middle

def put_in_order(graph,prints):
    # Now, I need to check if the request is in order, and if not, I need to put it in order

    middle = 0
    for l in prints: # I check all the prints
        so_far = [] # A list to store the numbers in order
        success = False
        for i in range(len(l)): # I go through the updates
            upcoming = l[i+1:] # I save a list of all the future updates
            if l[i] in graph and len(list(set(graph[l[i]]).intersection(set(upcoming)))) > 0:
                # If anything that would need to be completed first would appear later, this is impossible, I need to put it in order
                
                success = True
                remain = l[i:] # I need to keep track of what I have not sorted yet
                j = i
                while j <= len(l)//2: # I only need to find the middle element, so I only go until then
                    for left in range(0,len(l)-j):
                        # I go through the remaining updates, and and if there is something else that needs to be completed first, this cannot be the next, skip
                        if not len(list(set(graph[remain[left]]).intersection(set(remain) - {remain[left]}))) == 0:
                            continue
                        # Otherwise, this will work
                        l[j] = remain[left] # It will be the next update
                        remain.remove(remain[left]) # And it no longer needs to be sorted
                        break
                    j += 1
                break
        if success:
            middle += l[len(l)//2]
    return middle        
    
connections,prints = read_input()
graph = build_graph(connections) # I create a full graph out of the connections
print("Part 1:", in_order(graph, prints))
print("Part 2:", put_in_order(graph, prints))
