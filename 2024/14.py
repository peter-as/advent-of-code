from math import sqrt

def read_file() -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """
    Reads the location and velocity of the robots from the file

    Returns:
        A tuple of the list of locations of the robots, and the list of velocity of the robots
    """
    points = []
    velocity = []
    with open("2024/14.txt","r") as f:
        for i in f:
            l = i.split(",")
            p = (int(l[1].split(" ")[0]),int(l[0].split("=")[1]))
            v = (int(l[2]),int(l[1].split("=")[1]))
            points.append(p)
            velocity.append(v)
        return points, velocity

def move_robots(p: list[tuple[int, int]], v: list[tuple[int, int]], n: int, m: int, steps: int) -> dict[tuple[int, int], int]:
    """
    Simulates the movements of the robots and moves them 'steps' amount of times

    Args:
        p: The starting position of the robots
        v: The velocity of the robots
        n: The height of the board
        m: The width of the board
        steps: The amount of steps each robot takes

    Returns:
        A dictionary showing which position has how many robots on it
    """
    final_location = {}
    
    for i in range(len(p)):
        p_x, p_y = p[i]
        v_x, v_y = v[i]
        for time in range(steps):
            p_x = (p_x + v_x + n) % n
            p_y = (p_y + v_y + m) % m
        if ((p_x,p_y) in final_location):
            final_location[(p_x,p_y)] += 1
        else:
            final_location[(p_x,p_y)] = 1
    return final_location

def check_quadrants(n, m, points):
    """
    Counts how many robots are in each quadrants, and multiplies them together
    
    Args:
        n: The height of the board
        m: The width of the board
        points: the location 

    Returns: 
        The result of the multiplication of the quadrants
    """
    n_quad = n//2
    m_quad = m//2
    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0

    #TOP LEFT
    for i in range(n_quad):
        for j in range(m_quad):
            if (i,j) in points:
                top_left += points[(i,j)]
    #TOP RIGHT
    for i in range(n_quad):
        for j in range(m - m_quad, m):
            if (i,j) in points:
                top_right += points[(i,j)]
    #BOTTOM LEFT
    for i in range(n - n_quad, n):
        for j in range(m_quad):
            if (i,j) in points:
                bottom_left += points[(i,j)]
    #BOTTOM RIGHT
    for i in range(n - n_quad, n):
        for j in range(m - m_quad, m):
            if (i,j) in points:
                bottom_right += points[(i,j)]
    return top_left * top_right * bottom_left * bottom_right

def check_cluster(p: list[tuple[int, int]], v: list[tuple[int, int]], n: int, m: int, steps: int) -> list[tuple[int, int]]:
    """
    Simulates the movement of the robots, and stores the average total distance of each robot from their average coordinates

    Args:
        p: The starting position of the robots
        v: The velocity of the robots
        n: The height of the board
        m: The width of the board
        steps: The amount of steps each robot takes

    Returns:
        A list of tuples containing the total distance from the center point, and the number of steps taken so far
    """
    difference = []
    for time in range(steps):
        locations = []
        for i in range(len(p)):
            p_x, p_y = p[i]
            v_x, v_y = v[i]
            p_x = (p_x + v_x + n) % n
            p_y = (p_y + v_y + m) % m
            locations.append((p_x, p_y))
        distance = 0
        x = 0
        y = 0
        for k in locations:
            x += k[0]
            y += k[1]
        x /= len(locations)
        y /= len(locations)
        a = (x,y)
        for b in locations:
            distance += sqrt((a[0] - b[0])**2 + (a[1] - b[1]) ** 2)

        difference.append((distance, time+1))
        p = locations
    return difference

def visualize(n: int, m: int, final_locations: dict[tuple[int, int], int]) -> None:
    """
    Given the locations of robots, it visualizes the board on the console
    """
    for i in range(n):
        for j in range(m):
            if (i,j) in final_locations:
                print("+",end="")
            else:
                print(".",end="")
        print()
    

if __name__ == "__main__":
    n, m = 103, 101
    p, v = read_file()
    final_locations = move_robots(p, v, n, m, 100)
    print("Part 1:",check_quadrants(n, m, final_locations))

    differences = check_cluster(p, v, n, m, 10000)
    steps_to_take = min(differences)[1]
    final_locations = move_robots(p, v, n, m, steps_to_take)
    visualize(n, m, final_locations)
    print("Part 2:",steps_to_take)