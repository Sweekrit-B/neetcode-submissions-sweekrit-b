class MedianFinder:

    def __init__(self):
        self.stream = []
        self.num_vals = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.stream, num)
        print(self.stream)
        self.num_vals += 1
        return

    def findMedian(self) -> float:
        # print("Median index: ", self.num_vals // 2)
        first_half = heapq.nsmallest(self.num_vals // 2 + 1, self.stream)
        print(first_half)
        if self.num_vals % 2:
            return first_half[-1]
        else:
            return (first_half[-1] + first_half[-2]) / 2
        
        