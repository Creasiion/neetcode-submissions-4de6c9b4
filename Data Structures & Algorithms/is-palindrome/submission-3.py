class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_lower = ''.join(filter(lambda c: c.isalnum(), s.lower())) #Convert every character to lowercase since it is case-insensitive
        left = 0
        right = len(all_lower) - 1
        while left < right:
            if(all_lower[left] != all_lower[right]):
                return False
            left += 1
            right -= 1
        return True
        
