
class Solution:
    # O(n) time, O(n) space
    def containsDuplicateHashSet(self, nums: list[int]) -> bool:
        distinct_elements = set()

        for num in nums:
            if num in distinct_elements:
                return True
            distinct_elements.add(num)
        
        return False

    def containsDuplicateSorting(self, nums: list[int]) -> bool:
        n = len(nums)
        
        nums.sort()

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False

    def containsDuplicateBruteForce(self, nums: list[int]) -> bool:
        n = len(nums)

        for i in range(1, n):
            for j in range(i):
                if nums[i] == nums[j]:
                    return True

        return False

    