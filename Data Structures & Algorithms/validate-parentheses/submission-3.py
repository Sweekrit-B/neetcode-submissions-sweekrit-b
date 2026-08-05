# neetcode

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        relation = {')' : '(', ']' : '[', '}': '{'}

        for c in s:
            if c in relation:
                if stack and stack[-1] == relation[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
