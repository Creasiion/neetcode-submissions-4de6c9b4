class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Elements don't have to be in order in the array to make the sequence
        # Brute Force would be to sort the the elements, and then simply count up while keeping in mind 1>, but that'd be O(nlogn)
        # If we use hashing or a set, we could track that by checking if
        # i + 1 exist everytime - would need some kind of
        # currMax and curr, so we can compare the highest variables.
        # Considering frequency doesn't matter in this case (duplicates dont count), using a set could be fine
        # Think of possible sequence jumps - start of sequence would be
        # the next smallest num in the set, or if num -1 doesn't exist

        maxSeq = 0
        nums = set(nums)
        for num in nums:
            curr = 1
            if num - 1 not in nums: # Start of subseq
                for j in range(1, len(nums)):
                    if num + j in nums:
                        curr += 1
                    else:
                        break
            maxSeq = max(maxSeq, curr)
            
        return maxSeq

            
