class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_paren = []
        inter_str = []
        final_str = []
        for char in s:
            if char == "(":
                open_paren.append(len(inter_str))
                inter_str.append(char)
            elif char == ")":
                if len(open_paren) == 0: continue
                open_paren.pop()
                inter_str.append(char)
            else:
                inter_str.append(char)
        for i in range(len(inter_str))[::-1]:
            if open_paren and i == open_paren[-1]:
                open_paren.pop()
                continue
            final_str.append(inter_str[i])
        return "".join(final_str[::-1])
