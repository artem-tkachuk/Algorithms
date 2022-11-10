class Solution:
    # O(n) time | O(n) space
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        residuals = {} # map {value : index}

        for i in range(n):
            if nums[i] in residuals:
                return [residuals[nums[i]], i]
            else:
                residuals[target - nums[i]] = i
        
