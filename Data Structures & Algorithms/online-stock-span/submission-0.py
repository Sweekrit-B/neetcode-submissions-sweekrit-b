class StockSpanner:
    # monotonically increasing stack

    def __init__(self):
        self.stack = [] # stored as (price, span)

    def next(self, price: int) -> int:
        num_less = 1
        while self.stack and self.stack[-1][0] <= price:
            num_less += self.stack.pop()[1]
        self.stack.append((price, num_less))
        # print(self.stack)
        return num_less


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)