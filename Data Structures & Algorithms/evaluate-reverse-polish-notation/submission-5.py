class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea: add elements to the stack, remove top 2, perform operation, push back on
        stack = []
        if not tokens:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token == "+":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val + second_val)
            elif token == "*":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val * second_val)
            elif token == "-":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val - second_val)
            elif token == "/":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(int(first_val / second_val))
            else:
                stack.append(int(token))
        return stack[-1]