class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        left, right = 0, len(heights) - 1 
        while left < right :
            length = abs(left - right)
            width = min(heights[left], heights[right])
            curr_area = length * width 
            max_area = max(
                max_area, curr_area
            )
            if heights[left] < heights[right]:
                left+= 1 
            else:
                right -= 1 
        
        return max_area