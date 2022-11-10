class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndindHere = float('-inf')
        # Target return value: maximum sub of any subarray
        maxSoFar = float('-inf')

        for number in nums:
           maxEndindHere = max(number, maxEndindHere + number)
           maxSoFar = max(maxEndindHere, maxSoFar)

        return maxSoFar
