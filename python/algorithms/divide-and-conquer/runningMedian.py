class RunningMedian:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.lowerHalfMaxHeap = Heap(heapType="max")
        self.upperHalfMinHeap = Heap(heapType="min")

    def insert(self, number):
        # Choose a proper heap to insert the number to and insert it
        if number >= self.upperHalfMinHeap.peek():
            self.upperHalfMinHeap.insert(number)
        else:
            self.lowerHalfMaxHeap.insert(number)

        # If difference in sizes between the heaps is going to be > 1 after we've inserted, rebalance the heaps
        if abs(self.lowerHalfMaxHeap.getSize() - self.upperHalfMinHeap.getSize()) > 1:
            if self.lowerHalfMaxHeap.getSize() > self.upperHalfMinHeap.getSize():
                element_to_move = self.lowerHalfMaxHeap.remove()
                # TODO the newly added element is guaranteed to be the biggest/smallest in that new heap
                self.upperHalfMinHeap.insert(element_to_move)
            else:
                element_to_move = self.upperHalfMinHeap.remove()
                # TODO the newly added element is guaranteed to be the biggest/smallest in that new heap
                self.lowerHalfMaxHeap.insert(element_to_move)

        # Update the median
        if self.lowerHalfMaxHeap.getSize() == self.upperHalfMinHeap.getSize():  # even # of elements read so far
            self.median = (self.lowerHalfMaxHeap.peek() + self.upperHalfMinHeap.peek()) / 2
        else:  # odd number of elements read so far
            self.median = self.upperHalfMinHeap.peek() \
                if self.upperHalfMinHeap.getSize() > self.lowerHalfMaxHeap.getSize() \
                else self.lowerHalfMaxHeap.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, heapType):
        self.__heap = []
        self.__type = heapType
        self.__comparisonFunc = lambda a, b: (a >= b) if heapType == "min" else (a <= b)

    """ INTERNAL API """

    def __siftDown(self, index):
        # Write your code here.
        # TODO do we assume that the heap property for all other nodes holds when calling this method?
        # This check is to basically remove the malicious indices right away
        if index >= 0:
            n = self.getSize()

            c1_idx = 2 * index + 1  # child 1 index

            while c1_idx < n:
                c2_idx = c1_idx + 1  # child 2 index = 2 * index + 2

                swap_child_idx = c1_idx if \
                    (c2_idx >= n or not self.getComparisonFunc()(self.__heap[c1_idx], self.__heap[c2_idx])) \
                    else c2_idx

                if not self.getComparisonFunc()(self.__heap[index], self.__heap[swap_child_idx]):
                    break  # break the loop if already in the right position
                else:
                    swap(index, swap_child_idx, self.__heap)
                    index = swap_child_idx
                    c1_idx = 2 * index + 1

            # else:  # self.getType() == "max"
            #     while c1_idx < n:
            #         c2_idx = c1_idx + 1  # child 2 index = 2 * index + 2
            #
            #         max_child_idx = c1_idx if (c2_idx >= n or self.__heap[c1_idx] > self.__heap[c2_idx]) else c2_idx
            #
            #         if self.__heap[index] >= self.__heap[max_child_idx]:
            #             break  # break the loop if already in the right position
            #         else:
            #             swap(index, max_child_idx, self.__heap)
            #             index = max_child_idx
            #             c1_idx = 2 * index + 1

            return index

    # O(log(n)) time | O(1) space
    def __siftUp(self, index):
        # Write your code here.
        if 0 < index < self.getSize():
            parentIndex = (index - 1) // 2

            while index > 0 and self.getComparisonFunc()(self.__heap[parentIndex], self.__heap[index]):
                swap(parentIndex, index, self.__heap)
                index = parentIndex
                parentIndex = (index - 1) // 2

    """ EXTERNAL API """

    def insert(self, value):
        # Write your code here.
        self.__heap.append(value)  # append new value at the end
        n = self.getSize()  # updated length of the heap array
        self.__siftUp(n - 1)  # sift up the newly inserted last element to appropriate position

    def remove(self):
        n = self.getSize()
        if n > 0:
            # put the current min/max to the last rightmost position at the deepest level of the heap
            swap(0, n - 1, self.__heap)
            # get the last element, which now is the previous root of the heap
            removed_elem = self.__heap.pop()
            # put the element to the proper place
            self.__siftDown(0)
            # return the value we removed
            return removed_elem
        else:
            return None

    def peek(self):
        if self.__heap is not None and self.__heap != []:
            return self.__heap[0]
        else:
            return float("inf") if self.getType() == "max" else -1 * float("inf")  # if self.getType() == "min"

    # Getters
    def getSize(self):
        return len(self.__heap)

    def getComparisonFunc(self):
        return self.__comparisonFunc

    def getType(self):
        return self.__type


# static helper method
def swap(i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]


def test():
    median = RunningMedian()
    array = [5, 10, 100, 26, 75, 4, 14, 27, 36, 45]

    for i in range(len(array)):
        median.insert(array[i])
        print(f'===============================')
        print(f'sorted array so far: {sorted(array[:i + 1])}')
        print(f'median after inserting {array[i]} is = {median.getMedian()}')


test()
