class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedVal = n*(n+1)//2
        val = sum(nums)
        return expectedVal - val