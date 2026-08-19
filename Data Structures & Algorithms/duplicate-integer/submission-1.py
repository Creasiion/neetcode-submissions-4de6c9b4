from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = defaultdict(int)
        for num in nums:
            tracker[num] += 1
            if tracker[num] > 1:
                return True
        return False
        