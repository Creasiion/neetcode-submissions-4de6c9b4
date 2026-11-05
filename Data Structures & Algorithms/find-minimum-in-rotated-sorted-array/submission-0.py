class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        It's just like the other Rotated Array problem, BUT instead, we're looking for the smallest value
        Based on the hints, we find which side to eliminate. Maybe by
        comparing them with each other? Look at the smallest one first? 
        Or if we compare them with mid again, if we find one of them breaks the ascending flow, that means the pivot/the smallest is in that half
        i.e.
        [3,4,5,6,1,2]
        3->5 follows the ascension, but 5->2 breaks it
        We could update our result by doing min(currMin, nums[mid])
        Might not need a min tracker, but will keep for now!
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]: # Means the pivot starts here
                left = mid + 1
            else:
                right = mid
        return nums[left] 