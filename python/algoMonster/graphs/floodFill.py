from typing import List
from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    # What is our original color we are replacing?
    original_color = image[r][c]
    # Assuming num_rows >= 1, num_cols >= 1
    num_rows, num_cols = len(image), len(image[0])

    def get_valid_neighbors(image, position):
        # list of neighbors we will return (potentially empty)
        valid_neighbors = []
        # right, down, left, up -- could also add diagonal if it was allowed
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # row and column of where we stand
        (r, c) = position
        # apply each direction
        for (dr, dc) in directions:
            # new position
            (curr_r, curr_c) = r + dr, c + dc
            # check that it's valid
            if (curr_r in range(num_rows)) and (curr_c in range(num_cols)):
                # color at that position
                curr_color = image[curr_r][curr_c]
                # check that it is the same as original color
                if (curr_color == original_color): 
                    valid_neighbors.append((curr_r, curr_c))

        return valid_neighbors
    
    # We can run BFS
    def bfs(starting_position):
        queue = deque([starting_position])
        # Explore while there are no more nodes to explore
        while len(queue) > 0:
            # get the next position we explore
            position = queue.popleft()
            # parse out row and column individually
            (row, col) = position
            # overwrite the pixel with the replacement color
            image[row][col] = replacement
            # continue the same for the valid neighbors
            for neighbor in get_valid_neighbors(image, position):
                queue.append(neighbor)
    
    # Alternatively we can run DFS 
    def dfs(position):
        # get the specific coordinates for the position
        (row, col) = position
        # overwrite the pixel with the replacement color
        image[row][col] = replacement
        # continue the same for all the valid neighbors
        for neighbor in get_valid_neighbors(image, position):
            dfs(neighbor)

    # Do something only if we replace original color with a different one
    # Otherwise we would have to used the visited set
    if replacement != original_color:
        dfs((r, c)) 
    # return the (potentially) updated image to the caller
    return image

if __name__ == '__main__':
    r = 2
    c = 2
    replacement = 10
    image = [
        [0,1,3,4,1],
        [3,8,8,3,3],
        [6,7,8,8,3],
        [12,2,8,9,1],
        [12,3,1,3,2]
    ]
    result = flood_fill(r, c, replacement, image)
    for row in result:
        print('  '.join(map(str, row)))
