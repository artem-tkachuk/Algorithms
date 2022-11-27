class Solution:
    # O(n) time | O(1) space
    def trap(self, heights: list[int]) -> int:
        # total # of elements in the heights array
        n = len(heights)
        # left and right pointers
        left, right = 0, n - 1
        # maximum heights seen in subarray ending at left and subarray starting at right
        leftMax, rightMax = heights[left], heights[right]
        # accumulator variable for the total units of water we can trap
        total_water = 0
        # until two pointers meet somewhere
        while left < right:
            # right is at the current maximum, otherwise we would have moved it
            if leftMax <= rightMax:
                # move left pointer to the right
                left += 1
                # see if new height is the biggest so far
                leftMax = max(heights[left], leftMax)
                # if we didn't update the leftMax, it is smaller than rightMax
                # because rightMax is at heights[right], so it is safe to say 
                # that we can trap min(leftMax, rightMax) - heights[left]
                # which in this case is just leftMax - heights[left] since leftMax <= rightMax
                # if we did update leftMax to heights[left], this will be 0
                total_water += leftMax - heights[left]
            # if heights[left] > heights[right]:
            # left is at its current maximum, otherwise we would have moved it
            else:   
                # move the right pointer
                right -=1
                # see if new height is the biggest so far
                rightMax = max(heights[right], rightMax)
                # if we didn't update the leftMax, it is smaller than rightMax
                # because leftMax is at heights[left], so it is safe to say 
                # that we can trap min(leftMax, rightMax) - heights[right]
                # which in this case is just rightMax - heights[right] since leftMax > leftMax
                # if we did update rightMax to heights[right], this will be 0
                total_water += rightMax - heights[right]

        return total_water