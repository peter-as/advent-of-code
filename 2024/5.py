import copy

def read_input():
    f = open("5.txt","r")
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
    incoming = {}
    for i in connections:
        x, y = i[0], i[1]
        if y not in incoming:
            incoming[y] = [x]
        else:
            incoming[y].append(x)
    return incoming

def in_order(graph,prints):
    middle = 0
    for l in prints:
        g = copy.deepcopy(graph)
        success = True
        for i in range(len(l)):
            upcoming = l[i+1:]
            if l[i] in g and len(list(set(g[l[i]]).intersection(set(upcoming)))) > 0:
                success = False
                break
            for k in upcoming:
                if l[i] in g[k]:
                    g[k].remove(l[i])
        if success:
            middle += l[len(l)//2]
    return middle

def put_in_order(graph,prints):
    middle = 0
    for l in prints:
        g = copy.deepcopy(graph)
        so_far = []
        success = False
        for i in range(len(l)):
            upcoming = l[i+1:]
            if l[i] in g and len(list(set(g[l[i]]).intersection(set(upcoming)))) > 0:
                success = True
                remain = l[i:]
                j = i
                while j <= len(l)//2:
                    for left in range(0,len(l)-j):
                        if remain[left] not in g:
                            good = remain[left]
                        elif not len(list(set(g[remain[left]]).intersection(set(remain) - {remain[left]}))) == 0:
                            continue
                        good = remain[left]
                        l[j] = good
                        remain.remove(good)
                        for f in remain:
                            if good in g[f]:
                                g[f].remove(good)
                        break
                    j += 1
                break
            for k in upcoming:
                if l[i] in g[k]:
                    g[k].remove(l[i])
        if success:
            middle += l[len(l)//2]
    return middle        
    
connections,prints = read_input()
graph = build_graph(connections)
print("Part 1:", in_order(graph, prints))
print("Part 2:", put_in_order(graph, prints))
