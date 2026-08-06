class MedianFinder:
    # intuition: the median has a n values smaller than it and n values larger than it
    # left half values -> max heap, right half values -> min heap
    # how do we manage these two heaps? lets say we're adding a value val
        # if val > max left half heap --> add to right half heap
        # if val < min right half heap --> add to left half heap
        # if diff in lengths of left and right half > 1 -->
            # smaller heap pushes values to larger heap until they are only apart by 1
            # can always designate left half to be the larger one

    def __init__(self):
        # both initialized with inf to not be empty
        self.left = [float('inf')] # max heap
        self.right = [float('inf')] # min heap

    def addNum(self, num: int) -> None:
        # print("---BREAK ADD---")
        # print(f"Adding {num}")

        # print("Before")
        # print(f"Left: {self.left}")
        # print(f"Right: {self.right}")

        # add the number
        if num <= self.right[0]:
            heapq.heappush(self.left, -num)
        if num > -self.left[0]:
            heapq.heappush(self.right, num)
        
        # normalize the heaps
        if len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) - len(self.left) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))
        
        # print("After")
        # print(f"Left: {self.left}")
        # print(f"Right: {self.right}")

    def findMedian(self) -> float:
        # print("---BREAK MEDIAN---")
        # print("Finding median")
        # print(f"Left: {self.left}")
        # print(f"Right: {self.right}")

        if len(self.left) > len(self.right):
            # print(f"Median: {-self.left[0]}")
            return -self.left[0]
        elif len(self.right) > len(self.left):
            # print(f"Median: {self.right[0]}")
            return self.right[0]
        else:
            # print(f"Median: {(-self.left[0] + self.right[0])/2}")
            return (-self.left[0] + self.right[0])/2     
        