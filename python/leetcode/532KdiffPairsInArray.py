from typing import List
from collections import Counter

class Solution:
    # INCORRECT - TODO fix
    # def findPairs(self, nums: List[int], k: int) -> int:
    #     # initialize count
    #     count = 0

    #     if k == 0:
    #         nums_counter = Counter(nums)
    #         for c in nums_counter:
    #              if nums_counter[c] >= 2:
    #                 count += 1
    #     else:
    #         # number of elements in the array
    #         n = len(nums)
    #         # sort the nums array
    #         nums.sort()
    #         # initialize the two pointers
    #         l, r = 0, 0
    #         # go through the sorted numbers
    #         while r < n:
    #             if l == r:
    #                 r += 1
    #             else:
    #                 # what is the current difference?
    #                 curr_diff = abs(nums[l] - nums[r])
                    
    #                 if curr_diff == k:
    #                     # increment count
    #                     count += 1
    #                     # update pointers
    #                     l += 1
    #                     r += 1
    #                 elif curr_diff < k:
    #                     r += 1
    #                 # curr_diff > k
    #                 else:
    #                     l += 1
       
    #     return count

    # CORRECT
    def findPairs(self, nums: List[int], k: int) -> int:
         # final answer - how many pairs are there?
        count = 0

        # k == 0 is an inconvenient special case, so we can handle it separately
        if k == 0:
            nums_counter = Counter(nums)

            for c in nums_counter:
                 if nums_counter[c] >= 2:
                    count += 1

        # sign of k does not change anything with regards to the answer 
        # - only the order of elements in the pair
        else:
            # removes duplicates and keeps track of the visited numbers
            # helps avoid duplicate pairs
            nums_visited = {num: True for num in nums}

            for num in nums:
                next, prev = num + k, num - k
                # only use this number if it has not yet been counted
                if nums_visited[num]:
                    # see if a pair looking forward exists
                    if next in nums_visited and nums_visited[next]:
                        count += 1
                    # see if a pair looking backwards exists
                    if prev in nums_visited and nums_visited[prev]:
                        count += 1
                    # mark visited - meaning, not counted anymore for future pairs
                    nums_visited[num] = False

        return count

        


print(Solution().findPairs([3, 1, 4, 1, 5], k=2))
# print(Solution().findPairs([1, 2, 3, 4, 5], k=1))
# print(Solution().findPairs([1, 3, 1, 1, 3, 5, 4], k=0))