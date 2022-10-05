class BinarySearchTree():
    _item = None
    _parent = None
    _left = None
    _right = None
    _height = 0

    # Root node constructor
    def __init__(self, item):
        self._item = item
        self._height = 1

    @staticmethod
    def find(tree, key):
        if tree is None:
            return None
        elif tree.getItem() == key:
            return tree
        elif tree.getItem() < key:
            return BinarySearchTree.find(tree.getRightSubtree(), key)
        else:  # tree.getItem() > key
            return BinarySearchTree.find(tree.getLeftSubtree(), key)

    @staticmethod
    def find_minimum_node(tree):
        min_node = tree

        while min_node is not None and min_node.getLeftSubtree() is not None:
            min_node = min_node.getLeftSubtree()

        return min_node

    @staticmethod
    def find_maximum_node(tree):
        max_node = tree

        while max_node is not None and max_node.getRightSubtree() is not None:
            max_node = max_node.getRightSubtree()

        return max_node

    @staticmethod
    def pre_order_traversal(tree):
        if tree is not None:
            print(f" {tree.getItem()}", end='')  # Item Processing
            BinarySearchTree.pre_order_traversal(tree.getLeftSubtree())
            BinarySearchTree.pre_order_traversal(tree.getRightSubtree())

    @staticmethod
    def in_order_traversal(tree):
        if tree is not None:
            BinarySearchTree.in_order_traversal(tree.getLeftSubtree())
            print(f" {tree.getItem()} ", end='')  # Item Processing
            BinarySearchTree.in_order_traversal(tree.getRightSubtree())

    @staticmethod
    def post_order_traversal(tree):
        if tree is not None:
            BinarySearchTree.post_order_traversal(tree.getLeftSubtree())
            BinarySearchTree.post_order_traversal(tree.getRightSubtree())
            print(f" {tree.getItem()} ", end='')  # Item Processing

    @staticmethod
    def insert(tree, item):
        """
            This method should not be called on empty trees, because they get created by calling the constructor
        """
        if tree is None:
            return None

        if item < tree.getItem():
            if tree.getLeftSubtree() is None:
                tree.setLeftSubtree(item)
                tree.getLeftSubtree().setParent(tree)
            else:
                BinarySearchTree.insert(tree.getLeftSubtree(), item)
        else:  # item > tree.getItem():
            if tree.getRightSubtree() is None:
                tree.setRightSubtree(item)
                tree.getRightSubtree().setParent(tree)
            else:
                BinarySearchTree.insert(tree.getRightSubtree(), item)

        left_tree_height = tree.getLeftSubtree().getHeight() if tree.getLeftSubtree() is not None else 0
        right_tree_height = tree.getRightSubtree().getHeight() if tree.getRightSubtree() is not None else 0
        tree.setHeight(max(left_tree_height, right_tree_height) + 1)

    # TODO implement
    @staticmethod
    def breadth_first_traversal(tree):
        print(" " * tree.getHeight())
        print(f"{tree.getItem()}")

        tree.getHeight()

    # TODO implement
    def delete_node(self):
        pass

    # TODO implement
    def delete_tree(self):
        pass

    # Getters
    def getItem(self):
        return self._item

    def getParent(self):
        return self._parent

    def getRightSubtree(self):
        return self._right

    def getLeftSubtree(self):
        return self._left

    def getHeight(self):
        return self._height

    # Setters
    def setParent(self, parent):
        self._parent = parent

    def setItem(self, item):
        self._item = item

    def setLeftSubtree(self, item):
        self._left = BinarySearchTree(item)

    def setRightSubtree(self, item):
        self._right = BinarySearchTree(item)

    def setHeight(self, newHeight):
        self._height = newHeight


def main():
    tree = BinarySearchTree(2)
    BinarySearchTree.insert(tree, 3)
    # BinarySearchTree.in_order_traversal(tree)
    # BinarySearchTree.post_order_traversal(tree)
    BinarySearchTree.insert(tree, 1)
    print(f"In-order traversal:")
    BinarySearchTree.in_order_traversal(tree)

    min_node = BinarySearchTree.find_minimum_node(tree)
    print(f"\nThe minimum node is: {min_node.getItem()}")

    max_node = BinarySearchTree.find_maximum_node(tree)
    print(f"The maximum node is: {max_node.getItem()}")

    BinarySearchTree.insert(tree, -1)
    BinarySearchTree.insert(tree, 4)

    print(f"\nNew pre-order traversal:")
    BinarySearchTree.pre_order_traversal(tree)

    min_node = BinarySearchTree.find_minimum_node(tree)
    print(f"\nThe new minimum node is: {min_node.getItem()}")

    max_node = BinarySearchTree.find_maximum_node(tree)
    print(f"The new maximum node is: {max_node.getItem()}")

    node_val = 4
    node = BinarySearchTree.find(tree, node_val)
    print(f"Parent of {node_val} is {node.getParent().getItem()}")


main()
