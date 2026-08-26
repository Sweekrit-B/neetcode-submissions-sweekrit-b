class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr_str = ''

        for ch in path + "/":
            if ch == '/':
                if curr_str == '..':
                    if stack:
                        stack.pop()
                else:
                    if curr_str != '' and curr_str != '.':
                        stack.append(curr_str)
                curr_str = ''
            else:
                curr_str += ch

        return '/' + '/'.join(stack)        