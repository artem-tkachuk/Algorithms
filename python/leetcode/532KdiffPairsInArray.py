from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # number of elements in the array
        n = len(nums)
        # sort the nums array
        nums.sort()
        # initialize the two pointers
        l, r = 0, 0
        # initialize count
        count = 0
        # go through the sorted numbers
        while r < n:
            if l == r:
                r += 1
            else:
                # what is the current difference?
                curr_diff = abs(nums[l] - nums[r])
                
                if curr_diff == k:
                    # increment count
                    count += 1
                    # update pointers
                    l += 1
                    r += 1
                elif curr_diff < k:
                    r += 1
                # curr_diff > k
                else:
                    l += 1

        return count

print(Solution().findPairs([3, 1, 4, 1, 5], k=2))
print(Solution().findPairs([1, 2, 3, 4, 5], k=1))
print(Solution().findPairs([1, 3, 1, 5, 4], k=0))