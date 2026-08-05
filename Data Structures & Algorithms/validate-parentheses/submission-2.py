class Solution:
    def isValid(self, s: str) -> bool:
        open_ch = set(['[', '(', '{'])
        close_ch = set([']', ')', '}'])
        relation = {'(' : ')', '[' : ']', '{': '}'}
        
        stack = deque()
        for ch in s:
            if ch in open_ch:
                stack.append(ch)
            if ch in close_ch:
                if not stack:
                    return False
                most_recent_open_ch = stack.pop()
                if relation[most_recent_open_ch] != ch:
                    return False
        
        return True if not stack else False