from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Have a dict that tracks the value and it's frequency
        # freq needs to be sorted so that we can get the top k
        # If elements is sorted, we could always just keep track
        # while iterating through the array once. Since I have
        # No clue right now though, I'll do initial brute force
        # Is it possible to have an arr pairs ((num, freq)), and
        # sort/organize by freq this way?
        freq = Counter(nums)
        arr = []
        res = []
        for key, val in freq.items():
            arr.append((key,val))
        arr.sort(key = lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(arr[i][0])
        return res



        