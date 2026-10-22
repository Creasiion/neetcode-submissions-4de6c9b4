class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        amount = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            l = min(heights[left], heights[right])
            w = right - left
            amount = max(amount, l*w)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return amount
        