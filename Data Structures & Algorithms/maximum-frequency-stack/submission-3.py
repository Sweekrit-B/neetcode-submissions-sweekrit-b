class FreqStack:

    def __init__(self):
        self.stacks_per_freq = defaultdict(list)
        self.freq_per_val = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        new_freq = self.freq_per_val[val] + 1
        self.freq_per_val[val] = new_freq
        self.max_freq = max(new_freq, self.max_freq)
        self.stacks_per_freq[new_freq].append(val)
        # print(self.stacks_per_freq)

    def pop(self) -> int:
        max_freq_stack = self.stacks_per_freq[self.max_freq]
        popped = max_freq_stack.pop()
        if len(max_freq_stack) == 0:
            del self.stacks_per_freq[self.max_freq]
            self.max_freq -= 1
        self.freq_per_val[popped] -= 1
        return popped 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()