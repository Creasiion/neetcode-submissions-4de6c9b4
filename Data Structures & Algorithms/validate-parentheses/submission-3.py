class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #Push all open brackets into stack
        #Once it's a closed bracket, pop and check if it matches the pop
        #Return false whenever it doesn't match, end of for loop return true
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            if s[i] == ']':
                if not stack or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if not stack or stack.pop() != '{':
                    return False
            if s[i] == ')':
                if not stack or stack.pop() != '(':
                    return False

        return True if not stack else False #Stack should be empty by end of for loop
            
