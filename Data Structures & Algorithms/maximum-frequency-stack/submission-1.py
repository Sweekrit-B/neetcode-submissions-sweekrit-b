class FreqStack:

    def __init__(self):
        self.freq_stack = []
        self.added = 0
        self.freq_dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq_dict[val] += 1
        heapq.heappush(self.freq_stack, (-self.freq_dict[val], -self.added, val))
        self.added += 1
        # print(f"New heap: {self.freq_stack}")

    def pop(self) -> int:
        popped = heapq.heappop(self.freq_stack)
        # print(f"Heap after pop: {self.freq_stack}")
        self.freq_dict[popped[2]] -= 1
        return popped[2]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()