class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack where you store the number and the letter
        
        def update_stack(curr_val, stack):
            while stack and not stack[-1].isdigit():
                    curr_val = stack.pop() + curr_val
                    # print(f"Updating current value: {curr_val}")
            # at the end, you either have no stack left or a number
            if not stack:
                stack.append(curr_val)
                # print(f"Prev val is not a number, appending to stack as is: {stack}")
            else:
                stack.append(int(stack.pop()) * curr_val)
                # print(f"Prev val is number, appending to stack multipled: {stack}")

        stack = []
        curr_val = ""
        curr_val_num = True

        for i in s:
            if i.isdigit():
                if not curr_val_num and curr_val: # add the letters to the stack
                    stack.append(curr_val)
                    curr_val = ""
                curr_val_num = True
                curr_val += i
                # print(f"Current stack: {stack}")
                # print(f"Current val: {curr_val}, is a number")
            elif i not in "[1234567890]":
                if curr_val_num and curr_val: # add the numbers to the stack
                    stack.append(int(curr_val))
                    curr_val = ""
                curr_val_num = False
                curr_val += i
                # print(f"Current stack: {stack}")
                # print(f"Current val: {curr_val}, is not a number")
            elif i == "[":
                stack.append(curr_val)
                curr_val = ""
            elif i == "]":
                # take the last current element, which must be a string
                update_stack(curr_val, stack)
                curr_val = ""
        
        update_stack(curr_val, stack)
        return stack[0]