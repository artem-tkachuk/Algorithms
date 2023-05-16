# from typing import List
# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         counts_kv_list = list(map(lambda c: (c, counts[c]), counts))
#         counts_kv_list.sort(key=lambda kv: kv[1], reverse=True)
#         return list(map(lambda top_kv: top_kv[0], counts_kv_list[:k]))
    
# nums = [1,1,1,2,2,3]
# k = 2
# print(Solution().topKFrequent(nums, k))

from typing import List
from heapq import heapify, heappop, heappush
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []   # len(heap) == 0 at the beginning
        heapify(heap)

        for (ch, count) in counts.items():
            if len(heap) == k:
                # update value only if bigger than smallest
                # otherwise do nothing
                if count > heap[0][0]:   # count for top char of min heap
                    heappop(heap)
                    heappush(heap, (count, ch))
            else: # 0 <= len(heap) < k
                # always insert
                heappush(heap, (count, ch))

        output = []

        for _ in range(k):
            output.append(heappop(heap)[1]) # get the actual number, not its count

        return output