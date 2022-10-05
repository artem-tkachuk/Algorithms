from collections import defaultdict


def findConnectedComponents(graph):
    # make it a dictionary so it works with strings for node labels
    visited = {node: False for node in graph}
    components = defaultdict(list)
    count = 0

    # Helper function
    def explore(start):
        if visited[start]:
            return

        visited[start] = True
        print(start, end=' ')
        components[count].append(start)

        neighbours = graph[start]
        for node in neighbours:
            if not visited[node]:
                explore(node)

    for node in visited.keys():
        if not visited[node]:
            print(f"\nConnected component {count}:")
            explore(node)
            count += 1

    return count, components


def main():
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["B", "D"],
        "D": [],
        "F": ["E"],
        "E": []
    }

    count, components = findConnectedComponents(graph)

    print(f"\n{dict(components)}")


main()
