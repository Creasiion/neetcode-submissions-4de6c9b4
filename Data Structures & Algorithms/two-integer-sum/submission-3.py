class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea: Subtract nums[i] from target (to ensure we always get a smaller index), and then search if that value is inside the remaining of nums
        # How to make sure we don't use the same index?
        # Initial idea was to search pop current index arr in a copy, then find the target and it's index+1 that way
        # Maybe store number-index instead? Or index-number
        indexTracker = {} # key: value, value: index
        for i in range(len(nums)):
            diff = target - nums[i]
            if indexTracker:
                if diff in indexTracker and indexTracker[diff] != i:
                    return [indexTracker[diff], i]
            indexTracker[nums[i]] = i
            
