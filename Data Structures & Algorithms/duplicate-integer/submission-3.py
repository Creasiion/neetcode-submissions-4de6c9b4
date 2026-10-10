class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else: # If the number is in the tracker already, that means it appeared already, so no need to go thru the rest of the list
                return True
        return False
        