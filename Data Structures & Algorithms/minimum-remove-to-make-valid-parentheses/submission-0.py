from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_paren = []
        final_str = ""
        for char in s:
            if char == "(":
                open_paren.append(len(final_str))
                final_str += char
            elif char == ")":
                if len(open_paren) == 0: continue
                open_paren.pop()
                final_str += char
            else:
                final_str += char
        for paren in open_paren[::-1]:
            final_str = final_str[:paren] + final_str[paren + 1:]
        return final_str

