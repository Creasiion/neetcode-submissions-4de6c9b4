class Solution:
    def trap(self, height: List[int]) -> int:
        # IDEA: 2-ptr
        '''
        Water has to be in-between 2 non-zero bars, which is why in ex.1 the [0,2] doesn't count.
        We can get trapped water from the bars by getting Min(bar1, bar2). 
        When do we consider rain water filled an area? When the value between 2 points
        are LESS THAN them. I.e. 
        left = 1, right = 2, but in between is 3 is invalid. But if it was 0 it would have water filled with 1 block (since min(1,2) = 1)
        How do we calculate the water from the [3,1,0,1,3]?
        Based on my idea, [1,0,1] would be valid, and then the entirety [3,1,0,1,3] is
        With [1,0,1] it's just a length of 1, BUT with the bigger part of it it needs to account for the depth. I.e. if it was [3,0,0,0,3], water filled would be 9, BUT due to the inside, it's 7. 
        With that in mind maybe it's length (min(heights)) * width (distance of heights) - inner heights. But then how would we get inner heights? 
        Can figure out how much water to hold by min(heights)-innerHeight. I.e. for one of the 1's inside of the subarr, 3-1 = 2, which is how much water is in there.

        When to move left ptr? Condition could be when we find a 2 valid bars with a distance of more than 1
        STEPS:
        left = 0
        right = len(height) - 1
        leftMax
        rightMax
        while left < right
            check to update the tallest leftMax and right Max
            update water amount based on smallest height
            if height[leftMax] < height[rightMax]
                update water
                move left += 1
            else:
                update water
                move right -= 1
        '''

        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if leftMax < rightMax:
                water += leftMax - height[left]
                left += 1
            else:
                water += rightMax - height[right]
                right -= 1
        return water
