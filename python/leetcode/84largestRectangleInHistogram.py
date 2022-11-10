# This solution is too slow
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
       max_area, _ = self.largestRectangleAreaHelper(heights)
       return max_area

    def largestRectangleAreaHelper(self, heights: list[int]):
        n = len(heights)
        
        if n == 1:
            return (heights[0], heights[0])
        else:   # >= 2 
            left_max_area, left_min_height = self.largestRectangleAreaHelper(heights[1:])
            right_max_area, right_min_height = self.largestRectangleAreaHelper(heights[:-1])

            total_min_height = min(left_min_height, right_min_height)
            all_bars_max_area = total_min_height * n

            total_max_area = max(all_bars_max_area, left_max_area, right_max_area)
            
            return (total_max_area, total_min_height)

# print(Solution().largestRectangleArea([6,4]))
print(Solution().largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))