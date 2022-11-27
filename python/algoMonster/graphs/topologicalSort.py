from collections import defaultdict, deque

def topological_sort(graph: defaultdict(str)):
    # number of vertices in the graph
    num_vertices = len(graph)
    # Find out how many parents each vertex has
    counts = count_parents(graph)
    # Add all source vertices to the queue
    queue = deque([vertex for vertex in graph if counts[vertex] == 0])
    # resulting list we will return, if exists
    topological_ordering = []

    while len(queue) > 0:
        # get the vertex with 0 unvisited parents
        vertex = queue.popleft()
        # add it to the ordering
        topological_ordering.append(vertex)

        for child in get_children(graph, vertex):
            # decrement the count for this child because parent is visited
            counts[child] -= 1
            # see if we can now visit the child itself, and if so, add on the queue
            if counts[child] == 0:
                queue.append(child)
    
    # Ordering is complete only if all the vertices are in it 
    error_message = "Not a DAG ==> cycle ==> no topological ordering!"
    all_nodes_in_topological_ordering = len(topological_ordering) == num_vertices

    return topological_ordering if all_nodes_in_topological_ordering else error_message

def count_parents(graph: defaultdict(str)):
    counts = {vertex: 0 for vertex in graph}

    for vertex in graph:
        for neighbor in get_children(graph, vertex):
            counts[neighbor] += 1

    return counts
        

def get_children(graph: defaultdict(str), node: str):
    return graph[node]

if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }

    print(topological_sort(graph))