class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Idea: Since it's already sorted, AND we know that there's only 1 possible solution
        # That means we need to search the array for our 2 target numbers
        # Can use 2-ptr approch, and return [left, right] - will stop if left == right
        # If target is higher than left + right, then we move left,
        # Otherwise, move right 
        left = 0
        right = len(numbers) - 1

        while left < right:
            currPair = numbers[left] + numbers[right]
            if currPair == target:
                return [left+1, right+1] #Add 1 because they're 1-indexed
            elif target > currPair:
                left += 1
            else:
                right -= 1
        return []
        