from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case: If len(t) > len(s), then instantly return ''
        '''
        IDEA: If we have a counter for all of t's values, we can find/track a substring within s that has the amount of those values
        Theoretically, the minimum would be when s' freq has all the values of t's freq counter
        When would I shrink + expand?
        Could be like a previous sliding window problem, where the condition is actually our GOAL - so we shrink it right when we find a good length, and expand it afterwards to find strings again

        STEPS:
        - get freq of letters within t
        - have a result var to store substring
        - for right during the string
        -- append the current char until we have all amounts of chars from t - have a currStr variable
        -- then while loop for when we reach criteria
        --- update left AND our way of tracking letters of t within s
        -- end of for loop check min(len(result),len(currStr)), and replace result with whichever is smaller

        How would we keep track of t within s? S could have it's own freq counter for t characters, but maybe there's another way?
        '''
        if not t:
            return ''
        if len(t) > len(s):
            return ''
        criteria = Counter(t)
        currWindow = Counter()
        result = ''
        left = 0
        have = 0
        needCount = len(criteria)
        for right in range (len(s)):
            currWindow[s[right]] += 1

            if s[right] in criteria and currWindow[s[right]] == criteria[s[right]]:
                have += 1
            while have == needCount:
                if not result or right - left + 1 < len(result):
                    result = s[left:right + 1] 
                currWindow[s[left]] -= 1
                
                # Check if removing this character breaks a requirement
                if s[left] in criteria and currWindow[s[left]] < criteria[s[left]]:
                    have -= 1
                left += 1
            
        return result
