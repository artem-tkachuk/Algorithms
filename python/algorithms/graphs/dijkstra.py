def dijkstra():
    pass


def main():
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["B", "D"],
        "D": []
    }

    dijkstra(graph, startNode="A")


main()