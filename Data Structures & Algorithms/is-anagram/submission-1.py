from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: One string bigger than the other, return false
        # Could use counter from Collections and then compare their dictionary
        # Could also manually store

        if len(s) != len(t):
            return False

        sCount = Counter(s)
        tCount = Counter(t)
        
        for key, value in sCount.items():
            if key not in tCount: # Character isn't in string t
                return False
            if tCount[key] != value: # Freq of char differs
                return False
        return True
        