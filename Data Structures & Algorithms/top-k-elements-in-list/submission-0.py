class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        result = []
        count = 0
        counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        for key, val in counter:
            if count == k:
                return result
            else:
                result.append(key)
                count += 1
        return result