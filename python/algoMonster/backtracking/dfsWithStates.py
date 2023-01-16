from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    # Stack to hold current path
    path = []
    # list of all the paths we actually return
    res = []

    def dfs(startingNode):
        if all(child is None for child in startingNode.children):
            # root node, so a path is found
            res.append('->'.join(map(str, path)) + '->' + str(startingNode.val))
        else:
            # Go one level deeper
            path.append(startingNode.val)
            # process all children -- thus get all paths that include the current node
            for child in startingNode.children:
                dfs(child)
            # Remove the current node because all of its children are now processed
            path.pop()

    if root is not None:
        dfs(root)

    return res


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    root = build_tree(iter([1, 3, 2, 1, 5, 0, 3, 0, 4, 0]), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)














from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    res_paths = []

    def dfs(root, path):
        if all([node is None for node in root.children]):
            res_paths.append('->'.join(path) + '->' + str(root.val))
        else:
            for child in root.children:
                if child is not None:
                    dfs(child, path + [str(root.val)])

    return res_paths

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)

