class BrowserHistory:
    # essentially implementing a stack w/ a pointer
    # initialize the pointer at the end of the stack
    # back() -> moves pointer backwards by "steps" and returns the value there
    # forward() -> moves pointer forward by "steps" and returns the value there
    # visit() ->
        # clears everything in front of the current pointer
        # adds to the stack, moves pointer with it 
        # cannot just move the pointer, because then forward would be incorrect

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        # print("----VISIT----")
        self.pointer += 1
        if self.pointer >= len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.pointer] = url
        self.stack = self.stack[:self.pointer + 1] # the stack is only everything up to the pointer
        # print(f"Stack: {self.stack}, pointer: {self.pointer}")

    def back(self, steps: int) -> str:
        # print("----BACK----")
        # moves back at most to 0
        # print(f"Stack: {self.stack}")
        self.pointer = max(0, self.pointer - steps)
        # print(f"Moving pointer back to {self.pointer}, returning {self.stack[self.pointer]}")
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        # print("----FORWARD----")
        # moves forward at most to len(stack)-1
        # print(f"Stack: {self.stack}")
        self.pointer = min(len(self.stack)-1, self.pointer + steps)
        # print(f"Moving pointer forward to {self.pointer}, returning {self.stack[self.pointer]}")
        return self.stack[self.pointer]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)