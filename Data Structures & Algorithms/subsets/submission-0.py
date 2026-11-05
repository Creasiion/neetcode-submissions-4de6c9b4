class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        IDEA

        '''
        result = []

        def backtracking(start, currPath):
            result.append(list(currPath))
            for i in range(start, len(nums)):
                currPath.append(nums[i])
                backtracking(i+1, currPath)
                currPath.pop()
        
        backtracking(0,[])

        return result