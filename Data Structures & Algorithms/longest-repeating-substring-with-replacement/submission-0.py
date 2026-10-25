from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window - it fails when we can no longer switch k characters
        # Find the most frequent character in a substring, since that'll
        # Give us the least moves. Then our replacements would be
        # len(curr substring) - maxFreq. If that value is > K, then we can move the left pointer
        # Are we getting the maxFreq from that substring OR from the entire string? 
        # If we do the substring, then we would also need to update our tracker everytime the string shrinks/expands
        charCount = Counter()
        left = 0
        longestStr = 0
        for right in range(len(s)):
            charCount[s[right]] += 1
            mostFreq = max(charCount.values())
            while (right - left +1) - mostFreq > k:
                charCount[s[left]] -= 1
                left += 1
                mostFreq = max(charCount.values())
            longestStr = max(longestStr, right-left+1)
        return longestStr