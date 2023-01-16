from collections import deque

def bfs(graph, startNode, target):
    # get the children for a specific node
    def get_children(node):
        return graph[node]
    # start with the startNode in the queue
    # no visited set because we cannot have cycles
    queue = deque([startNode])
    # continue the search until all the node in the startNode's connected component
    # are not explored
    while len(queue) > 0:
        # dequeue the next node
        node = queue.popleft()
        # visit the node and terminate early if needed
        if node == target:
            return "Found!"
        else:
            # enqueue children to to continue the search
            for child in get_children(node):
                queue.append(child)

    return f"Node {target} is not in the graph or is unreachable from {startNode}!"



if __name__ == '__main__':
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["B", "D"],
        "D": []
    }

    print(bfs(graph, "C", "D"))

            