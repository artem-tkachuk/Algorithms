# Works on both directed and undirected graphs
def bfs(graph, startNode):
    # return array
    arr = []
    # Don't perform BFS on an empty graph or invalid start node
    if graph is None or startNode is None or startNode not in graph:
        return False

    queue = [startNode]
    queued = {node: False for node in graph}
    queued[startNode] = True

    while len(queue) != 0:
        # Pop the FIRST element of the queue
        # Queue at this point is guaranteed to be non-empty
        node = queue.pop(0)
        # Visit/Process the current node
        print(f"{node}", end=' ')
        arr.append(node)
        # Add all nodes which current node is connected to to the queue
        for child in graph[node]:
            if not queued[child]:
                queue.append(child)
                queued[child] = True

    return arr


def main():
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "E"],
        "C": ["A", "B", "D"],
        "D": ["C"],
        "E": ["B"]
    }
    #        A
    #       |  \
    #    E--B--C
    #          |
    #          D
    # Expected output: A B C E D

    result = bfs(graph, startNode="A")
    print(f"\nReceived output: {result}\n")
    print('Expected output: ["A", "B", "C", "E", "D"]\n')


main()
