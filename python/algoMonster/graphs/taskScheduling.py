from typing import List
from collections import defaultdict, deque

def topological_sort(graph: defaultdict(list)):
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

def count_parents(graph: defaultdict(list)):
    counts = {vertex: 0 for vertex in graph}

    for vertex in graph:
        for neighbor in get_children(graph, vertex):
            counts[neighbor] += 1

    return counts


def get_children(graph: defaultdict(list), node: str):
    return graph[node]

def build_graph(tasks: List[str], requirements: List[List[str]]):
    # This can't be defaultdict(list) because there will be no entry for sink nodes
    # and the total # of vertices obtained through len(graph) will be incorrect
    graph = {vertex: [] for vertex in tasks}
    
    for (startNode, endNode) in requirements:
        graph[startNode].append(endNode)

    return graph

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    graph = build_graph(tasks, requirements)
    task_schedule = topological_sort(graph)
    # There is guaranteed to be a solution, so no need for validation
    return task_schedule

if __name__ == '__main__':
    tasks = ["a", "b", "c", "d"]
    requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f'output size {len(res)} does not match input size {len(tasks)}')
        exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            exit()
    print(f'The topological ordering is {res}')
    print('ok')
