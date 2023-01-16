from typing import List, Tuple
from collections import deque

def get_neighbors(grid: List[List[int]], point: Tuple[int, int]):
    # sizes of the grid
    num_rows, num_cols = len(grid), len(grid[0])
    # where we stand
    curr_x, curr_y = point
    # input validation -- we want it to be inside the board!
    if curr_x not in range(num_cols) or curr_y not in range(num_rows):
        return "Invalid point!"
    # all legal moves from (0, 0) -- can also add digonal if wanted/needed
    deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # list of valid neighbor coordinates that we return
    neighbor_coordinates = []
    # apply each delta
    for dx, dy in deltas:
        # get the coordinate for this neighbor
        x, y = curr_x + dx, curr_y + dy
        # Validate whether this neighbor is allowed or not
        if y in range(num_rows) and x in range(num_cols) and grid[y][x] != -1:
            neighbor_coordinates.append((y, x))
    
    return neighbor_coordinates


def bfs(grid, starting_point):
    queue = deque([starting_point])
    visited = set([starting_point])

    while len(queue) > 0:
        # dequeue the next point to explore
        point = queue.popleft()
        # parse out the coordinates
        y, x = point
        # Visit the vertex
        print(f'{point}: {grid[y][x]}')
        # explore neighbors
        for neighbor in get_neighbors(grid, point):
            if neighbor not in visited:
                # Enqueue and visit the neighbor if not already visited
                queue.append(neighbor)
                visited.add(neighbor)

if __name__ == "__main__":
    grid = [
        [0, 0, -1],
        [0, 0, 0],
        [0, 0, 0]
    ]

    point = (1, 1)

    bfs(grid, point)