import heapq

def dijkstra(graphEdges, start, goal):
    # graphEdges: List[List[List[destination, distance]]
    # list of outgoing edges for each node in a graph
    # every edge is [destination, distance]


    # tent_distances = {node: float('inf') for node in range(num_nodes)}
    num_nodes = len(graphEdges)

    visited = {node: False for node in range(num_nodes)}
    visited[start] = True

    dist_heap = MinHeap([(start, 0)])

    while not visited[goal]:
        curr_node = dist_heap.remove()

        for outgoing_edge in graphEdges[curr_node]:
            [neighbor, distance_from_curr] = outgoing_edge
            if not visited[neighbor]:  # if the destination node is not already visited
                calculated_dist = tent_distances[curr_node] + distance_from_curr

                if calculated_dist < tent_distances[neighbor]:
                    tent_distances[neighbor] = calculated_dist


def main():
    # Adjacency list representation of a graph
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["B", "D"],
        "D": []
    }

    dijkstra(graph, start="A", goal="D")


main()









# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

# static methods
# O(1) time, O(1) space
def swap(i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.__buildHeap(array)

    """
        INTERNAL API
    """
    # Implementation using siftDown(), O(n) time, O(1) space
    def __buildHeap(self, array):
        self.heap = array

        n = self.getLength()
        # index of last element - 1 = (n - 1) - 1 = n - 2
        parentIndex = (n - 2) // 2
        # [0, parentIndex] -- all nodes are parents from this moment
        for i in reversed(range(parentIndex + 1)):
            self.__siftDown(i)

        return self.heap

    # implementation using siftUp(), O(n log(n)) time | O(1) space since all actions are in-place
    # def __buildHeap(self, array):
    #     # Write your code here.
    #     self.heap = array
    #
    #     for i in range(1, len(array)):
    #         self.__siftUp(i)
    #
    #     return self.heap

    # O(log(n)) time | O(1) space
    # def __siftDown(self, index):
    #     # Write your code here.
    #     # TODO do we assume that the heap property for all other nodes holds when calling this method?
    #     if index >= 0:
    #         n = self.getLength()
    #
    #         while index < n - 1:
    #             c1_idx = 2 * index + 1  # child 1 index
    #             c2_idx = 2 * index + 2  # child 2 index
    #             child_indices = [c1_idx, c2_idx]
    #
    #             c1 = self.heap[c1_idx] if c1_idx < n else float('inf')  # child 1's value (if applicable)
    #             c2 = self.heap[c2_idx] if c2_idx < n else float('inf')  # child 2's value (if applicable)
    #             children = [c1, c2]
    #
    #             if self.heap[index] <= min(children):
    #                 break
    #             else:
    #                 min_child_idx = child_indices[0 if c1 < c2 else 1]
    #                 swap(index, min_child_idx, self.heap)
    #                 index = min_child_idx
    #
    #         return index
    #
    #

    # O(log(n)) time | O(1) space
    def __siftDown(self, index):
        # Write your code here.
        # TODO do we assume that the heap property for all other nodes holds when calling this method?
        # This check is to basically remove the malicious indices right away
        if index >= 0:
            n = self.getLength()

            c1_idx = 2 * index + 1  # child 1 index

            while c1_idx < n:
                c2_idx = c1_idx + 1  # child 2 index = 2 * index + 2

                min_child_idx = c1_idx if (c2_idx >= n or self.heap[c1_idx] < self.heap[c2_idx]) else c2_idx

                if self.heap[index] <= self.heap[min_child_idx]:
                    break   # break the loop if already in the right position
                else:
                    swap(index, min_child_idx, self.heap)
                    index = min_child_idx
                    c1_idx = 2 * index + 1

            return index

    # O(log(n)) time | O(1) space
    def __siftUp(self, index):
        # Write your code here.
        if 0 < index < self.getLength():
            parentIndex = (index - 1) // 2

            while index > 0 and self.heap[parentIndex] > self.heap[index]:
                swap(parentIndex, index, self.heap)
                index = parentIndex
                parentIndex = (index - 1) // 2

    """
        EXTERNAL API
    """
    # O(1) time | O(1) space
    def peek(self):
        # Write your code here.
        if self.heap is None or self.heap == []:
            return None
        else:
            return self.heap[0]

    # O(log(n)) time, O(1) time
    def remove(self):
        # Write your code here.
        n = self.getLength()
        # put the current min to the last rightmost position at the deepest level of the heap
        swap(0, n - 1, self.heap)
        # get the last element, which now is the previous root of the heap
        removed_min = self.heap.pop()
        # put the element to the proper place
        self.__siftDown(0)
        # return the value we removed
        return removed_min

    # O(log(n)) | O(1) time
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)  # append new value at the end
        n = self.getLength()  # updated length of the heap array
        self.__siftUp(n - 1)  # sift up the newly inserted last element to appropriate position

    # My helper methods
    # O(1) time | O(1) space
    def getLength(self):
        return len(self.heap)
