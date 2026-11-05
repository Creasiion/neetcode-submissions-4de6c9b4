class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        IDEA
        Involved recursion or backtracking since we want combinations - we want UNIQUE combinations
        "Two combinations are the same if the frequency of each of the chosen numbers is the same"
        Similar to subsets problem, but this time we DO have a condition to stop the backtracking at
        '''
        result = []

        def backtracking(start, currPath,currSum):
            if currSum == target:
                result.append(list(currPath))
            elif currSum < target:
                for i in range(start, len(nums)):
                    currPath.append(nums[i])
                    backtracking(i, currPath, currSum + nums[i])
                    currPath.pop()

        backtracking(0, [], 0)
        return result

        