def dfs(graph, startNode):
    # make it a dictionary so it works with strings for node labels
    visited = {node: False for node in graph}

    def explore(node):
        if visited[node]:
            return
        # Visit a node
        visited[node] = True
        print(node, end=' ')
        # Visit neighbours
        neighbours = graph[node]
        for node in neighbours:
            if not visited[node]:
                explore(node)

    explore(startNode)


def main():
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["B", "D"],
        "D": []
    }

    dfs(graph, startNode="A")


main()
