class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # IDEA: 2 pointer approach but also with length and width in mind
        # Technically the highest would've been the higher length x width number if not for the poles
        # But since they're different, we need to keep track of which of the 2 poles is smaller for length (using min left vs right), then find the width 
        amount = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            length = min(heights[left], heights[right]) # Smallest of the 2 bars we're looking at
            width = right - left # Distance of the bars we're at
            amount = max(amount, length*width)
            if heights[left] > heights[right]: # Move the smallest bar to the next one
                right -= 1
            else:
                left += 1
        return amount
        