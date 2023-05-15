from heapq import heappush, heappop, heapify

class MedianOfStream:
    def __init__(self) -> None:
        self.total = 0

        self.min_heap = []
        self.max_heap = []

        heapify(self.min_heap)
        heapify(self.max_heap)

    def peek(self, heap, type):
        if heap is None:
            return None
        else:
            if type == 'min':
                return heap[0]
            elif type == 'max':
                return -heap[0]
            else:
                print('Error')

    def _rebalance(self):
        if len(self.max_heap) > len(self.min_heap):
            top_of_max_heap = -heappop(self.max_heap)
            heappush(self.min_heap, top_of_max_heap)

        elif len(self.min_heap) - len(self.max_heap) > 1:
            top_of_min_heap = heappop(self.min_heap)
            heappush(self.max_heap, -top_of_min_heap)

        # at this point either 
        # len(max_heap) == len(min_heap) ==> median is average of two tops
        #   or 
        #      len(max_heap) + 1 == len(min_heap) ==> median is top of min_heap

    def add_number(self, num: float) -> None:
        # WRITE YOUR BRILLIANT CODE HERE
        if len(self.min_heap) == 0 or num >= self.peek(self.min_heap, 'min'):
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        
        self._rebalance()

    def get_median(self) -> float:
        # ALSO HERE
        # odd number of elements
        heaps_are_equal = len(self.min_heap) == len(self.max_heap)

        if heaps_are_equal:
            return (self.peek(self.min_heap, 'min') + self.peek(self.max_heap, 'max')) / 2
        else:
            return self.peek(self.min_heap, 'min')        

if __name__ == '__main__':
    median_of_stream = MedianOfStream()
    n = 7
    input = [
        '12', '4', 'get', '10', '555', 'get', '66' ,'13', 'get'
    ]

    for line in input:
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)
