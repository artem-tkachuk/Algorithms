from typing import List
from collections import deque

def shortest_path(graph: List[List[int]], start_vertex: int, end_vertex: int) -> int:

    def get_neighbors(of):
        return graph[of]

    level = 0

    visited = set([start_vertex])
    queue = deque([start_vertex])

    while len(queue) > 0:
        # explore all the vertices_in_queue nodes in the current level
        vertices_in_queue = len(queue)

        for _ in range(vertices_in_queue):
            # Pop the vertex from the queue
            vertex = queue.popleft()
            # Visit the vertex 
            # print(vertex, end=' ')  # debugging
            # if we found the target vertex
            if vertex == end_vertex:
                # return how far it was from the start
                return level
            else:
                # add neighbors to the queue
                for neighbor in get_neighbors(of=vertex):
                    # if they were not already visited
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(vertex)
        # increment level to indicate that we already explored the nodes
        # at the current level and haven't found the target one yet
        level += 1

    # if we didn't return up to this point
    # indicate that the node is not in the graoh
    return -1
    

if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }

    a = 2
    b = 3
    res = shortest_path(graph, a, b)
    print(f'Shortest path from {a} to {b} is {res}')
