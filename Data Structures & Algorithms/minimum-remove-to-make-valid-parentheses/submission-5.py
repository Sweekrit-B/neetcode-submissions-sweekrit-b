class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_paren = []
        skip = set()

        for i, char in enumerate(s):
            if char == "(":
                open_paren.append(i)
            elif char == ")":
                if not open_paren:
                    skip.add(i)
                else:
                    open_paren.pop()
        skip.update(open_paren)

        return ''.join(ch for i, ch in enumerate(s) if i not in skip)
