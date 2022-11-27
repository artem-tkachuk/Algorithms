class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxEndindHere = float('-inf')
        # Target return value: maximum sub of any subarray
        maxSoFar = float('-inf')

        for number in nums:
           maxEndindHere = max(number, maxEndindHere + number)
           maxSoFar = max(maxEndindHere, maxSoFar)

        return maxSoFar

    def maxSubArrayDivideAndConquer(self, nums: list[int]) -> int:
        n = len(nums)
        return self.maxSubArrayDivideAndConquerHelper(nums, 0, n)
        

    def maxSubArrayDivideAndConquerHelper(self, nums: list[int], left: int, right: int):
        if left > right - 1:
            return float('-inf')
        elif left == right - 1: # single element
            return nums[left]
        else:  # left < right - 1
            # get the index of the middle of the array, rounded down
            midpoint_index = (left + right) // 2
            # get the maximum subarray from the elements only from the left half
            maximum_sum_only_left = self.maxSubArrayDivideAndConquerHelper(nums, left=0, right=midpoint_index)
            # get the maximum subarray from the elements only from the right half
            maximum_sum_only_right = self.maxSubArrayDivideAndConquerHelper(nums, left=midpoint_index + 1, right=right)
            # compute the maximum subarray from elements always including the middle element
            maximum_sum_contiguous_left = 0
            curr_sum_contiguous_left = 0
            # go from (midpoint - 1) to 0
            for i in range(midpoint_index - 1, -1, -1): 
                curr_sum_contiguous_left += nums[i]
                maximum_sum_contiguous_left = max(maximum_sum_contiguous_left, curr_sum_contiguous_left)
            # maximum sum subarray with right half and always including 
            # the middle element and maximum subarray from left half as well
            maximum_sum_contiguous_right = 0
            curr_sum_contiguous_right = 0
            # go from (midpoint - 1) to 0
            for i in range(midpoint_index + 1, right): 
                curr_sum_contiguous_right += nums[i]
                maximum_sum_contiguous_right = max(maximum_sum_contiguous_right, curr_sum_contiguous_right)
            
            # maximum sum subarray with left half and always including the middle element
            middle_elem = nums[midpoint_index]
            maximum_sum_all = maximum_sum_contiguous_left + middle_elem + maximum_sum_contiguous_right 
            # return the total maximum sum
            return max(maximum_sum_only_left, maximum_sum_all, maximum_sum_only_right)


print(Solution().maxSubArrayDivideAndConquer([-2, 7, -2, 8]))