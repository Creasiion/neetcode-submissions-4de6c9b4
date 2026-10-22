from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We care about the length moreso than what the
        # Actual string is, so we can just return an int to save space
        # Idea: have a kind of subarray that keeps track of the current
        # substring we're on - subwindow
        # Expand window AND currMax count (move right) when there's no duplicates
        # Shrink when there is a duplicate (move left)
        # Can have a freq counter, so then we know when there's a duplicate character
        left = 0
        currStr = Counter()
        totalMax = 0
        currLen = 0

        for right in range(len(s)):
            currStr[s[right]] += 1 # techncically, the only character that would have a duplicate would be due to the last value we add to the array
            currLen += 1
            while currStr[s[right]] != 1:
                currStr[s[left]] -= 1 # Remove value at the current left
                left += 1 # Go to next left value
                currLen -= 1 # Decrease current length tracker
            totalMax = max(totalMax, currLen)
        return totalMax
        