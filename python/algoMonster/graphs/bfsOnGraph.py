from collections import deque

def bfs(graph, starting_vertex):
    queue = deque([starting_vertex])
    visited = set()

    while len(queue) > 0:
        vertex = queue.popleft()
        # Visit the vertex
        print(vertex)
        visited.add(vertex)
        # explore neighbors
        for neighbor in get_neighbors(graph, vertex):
            if neighbor not in visited:
                queue.append(neighbor)

def bfs_with_level_count(graph, starting_vertex):
    queue = deque([starting_vertex])
    visited = set()
    level = 0

    while len(queue) > 0:
        # invariant: we enter the new loop iteration with all the nodes from the previous level being on the queue
        num_nodes_in_queue = len(queue)
        print(f'level {level}:')
        for _ in range(num_nodes_in_queue):
            vertex = queue.popleft()
            # Visit the vertex
            print(vertex)
            visited.add(vertex)
            # explore neighbors
            for neighbor in get_neighbors(graph, vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
        # increment the level since we are going to a new level at this point
        level += 1


def get_neighbors(graph, vertex):
    return graph[vertex]


if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D"],
        "D": ["A"]
    }

    bfs_with_level_count(graph, "C")