from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter()
        res = []
        remaining = 0
        for number in nums:
            count[number] += 1
        while remaining < k:
            highest = max(count, key=count.get)
            res.append(highest)
            count.pop(highest)
            remaining +=1

        return res