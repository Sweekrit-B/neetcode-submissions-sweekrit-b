class Solution:
    def simplifyPath(self, path: str) -> str:
        # as you iterate through a path, lets say you arrive at a "/"
            # any "." beneath it gets squished
            # after that, any "/" get squished
        
        def remove_until_n_backslashes_gone(n, stack):
            num_removed = 0
            while stack and num_removed != n:
                removed = stack.pop()
                if removed == "/":
                    num_removed += 1
            return stack
        
        stack = []
        num_dots = 0
        dir_prev_valid = False
        for ch in path:
            if ch == "." and dir_prev_valid:
                num_dots += 1
            else:
                if ch == "/":
                    dir_prev_valid = True
                    while stack and stack[-1] == "/":
                        stack.pop()
                    if stack and stack[-1] == "." and num_dots <= 2:
                        remove_until_n_backslashes_gone(num_dots, stack)
                else:
                    dir_prev_valid = False
                num_dots = 0
            stack.append(ch)
            # print(stack)
        
        while stack and stack[-1] == "/":
            stack.pop()
        if stack and stack[-1] == "." and num_dots <= 2 and dir_prev_valid:
            remove_until_n_backslashes_gone(num_dots, stack)

        return ''.join(stack) if stack else '/'