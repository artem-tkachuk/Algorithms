# O(n) time | O(1) space
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = [1] * n
        prefixProd, postfixProd = 1, 1
        
        for left in range(n):
            right = n - 1 - left
            # Update the final out array
            out[left] *= prefixProd
            out[right] *= postfixProd
            # Update the left and right running products
            prefixProd *= nums[left]
            postfixProd *= nums[right]

        return out