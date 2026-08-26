class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr_str = ''

        for ch in path:
            if ch == '/':
                if curr_str == '..':
                    if stack:
                        # print("Popping at /: ", stack[-1])
                        stack.pop()
                        # print("Current stack: ", stack)
                else:
                    if curr_str != '' and curr_str != '.':
                        # print("Current string at /: ", curr_str)
                        stack.append(curr_str)
                        # print("Current stack: ", stack)
                curr_str = ''
            else:
                curr_str += ch
                # print("Current string: ", curr_str)
        
        # print("Final stack: ", stack)

        if stack and curr_str == '..':
            # print("Popping:", stack[-1])
            stack.pop()
        else:
            if curr_str != '' and curr_str != '.':
                print(curr_str)
                stack.append(curr_str)

        return '/' + '/'.join(stack)        