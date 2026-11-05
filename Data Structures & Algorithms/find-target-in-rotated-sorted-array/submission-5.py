class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Idea: still start from the center
        BUT instead of instantly going left or right based on the target, we would need to compare the current values of left and right
        - Find the target, check if mid is less than/greater than it
        - Where do we go? Based on that, we see which side would be ascending vs which side is descending
        - How to tell though? We could compare left vs right itself, or compare them with middle
        e.x.
        [3,4,5,6,1,2]
        left = 3, right = 2, mid = 5
        left > right, so we can assume that the left side is the one with greater values than right
        Alternative, can see if it goes left -> mid in size or mid -> right in size, since it was prev in ascended order. In this case left -> works ascendingly and not mid -> right
        '''
        left = 0
        right = len(nums) - 1
        res = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            

            if nums[left] <= nums[mid]: # leftside is still in ascending order
                if nums[left] <= target <= nums[mid]: # See if target is within this range
                    right = mid - 1 # shrink right to be within left-mid range
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1


        return res