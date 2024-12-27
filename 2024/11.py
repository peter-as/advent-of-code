from collections import defaultdict

def read_file():
    f = open("11.txt","r")
    line = [int(x) for x in f.read().split()]
    d = defaultdict(int)
    for i in line:
        d[i] += 1
    return d


def transform_stones(rocks, times):
    for blink in range(times):
        change = defaultdict(int)
        for i in rocks:
            change[i] -= rocks[i]
            if i == 0:
                change[1] += rocks[i]
            elif len(str(i)) % 2 == 0:
                divider = int(10 ** (len(str(i))/2))
                f,s = i // divider, i % divider
                change[f] += rocks[i]
                change[s] += rocks[i]
            else:
                change[i * 2024] += rocks[i]
        for i in change:
            rocks[i] += change[i]
    sum = 0
    for i in rocks:
        sum += rocks[i]
    return sum
    
rocks = read_file()
print("Part 1:", transform_stones(rocks,25))
rocks = read_file()
print("Part 2:", transform_stones(rocks,75))
