class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        IDEA
        This one is like subsets, BUT we don't care about uniques subsets like it did, and we care about the length of the result
        Condition must be currPath == len(nums)
        This would be like going to 1, branching between going to 2 or 3 next, and then picking the missing one before going to the next start value
        e.x.
        1
        /\
        [1,2] [1,3]
        /        \
        [1,2,3]   [1,3,2]

        How would we go to 1,3,2 though?
        Don't need start in this case, since
        '''
        result = []

        def backtracking(currPath):
            if len(currPath) == len(nums):
                result.append(list(currPath))
            else:
                for i in range(len(nums)):
                    if nums[i] not in currPath:
                        currPath.append(nums[i])
                        backtracking(currPath)
                        currPath.pop()

        backtracking([])
        return result