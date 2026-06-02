class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Idea: Start from the center
        # Two pointers, one going left, and the other going right
        # If they're the same value, then it's still a valid palindrome
        # Update string with the character on both sides
        # But what if the palindrome doesn't start in the center?
        n = len(s)
        longest = ''

        if n == 1:
            return s
        
        for i in range(len(s)):
            # odd case
            left = i
            right = i
            while left >= 0 and right <= n-1 and s[left] == s[right] :
                curr = s[left:right+1]
                longest = max(curr, longest, key=len)
                left -= 1
                right += 1

            # even case
            left = i
            right = i + 1
            while left >= 0 and right <= n-1 and s[left] == s[right] :
                curr = s[left:right+1]
                longest = max(curr, longest, key=len)
                left -= 1
                right += 1
        
        return longest
                
