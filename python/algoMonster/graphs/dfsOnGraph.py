def dfs(graph, starting_vertex):
    visited = set()

    def explore(vertex):
        # Visit the vertex
        print(vertex)
        visited.add(vertex)
        # explore neighbors
        for neighbor in get_neighbors(vertex):
            if neighbor not in visited:
                explore(neighbor)

    def get_neighbors(vertex):
        return graph[vertex]

    explore(starting_vertex)
        

if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D"],
        "D": ["A"]
    }

    dfs(graph, "C")