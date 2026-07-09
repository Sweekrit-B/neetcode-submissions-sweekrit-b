class MedianFinder:

    def __init__(self):
        self.firsthalf = []
        self.secondhalf = []
        self.currMedian = None
        self.currLen = 0

    def addNum(self, num: int) -> None:
        if len(self.firsthalf) == 0 and len(self.secondhalf) == 0:
            heapq.heappush(self.firsthalf, -num)
            self.currMedian = num
            self.currLen += 1
            print(f"First num. Current first half: {self.firsthalf}, current second half: {self.secondhalf}, current median: {self.currMedian}, current length: {self.currLen}")
            return

        print(f"Current median: {self.currMedian}")
        if num >= self.currMedian:
            heapq.heappush(self.secondhalf, num)
            print(f"2nd half addition. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
            self.currLen += 1
            print(f"Incrementing current length: {self.currLen}")
            if len(self.secondhalf) > math.ceil(self.currLen / 2):
                smallest = heapq.heappop(self.secondhalf)
                heapq.heappush(self.firsthalf, -smallest)
                print(f"2nd half reshuffling. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
        if num < self.currMedian:
            heapq.heappush(self.firsthalf, -num)
            print(f"1st half addition. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
            self.currLen += 1
            print(f"Incrementing current length: {self.currLen}")
            if len(self.firsthalf) > math.ceil(self.currLen / 2):
                largest = heapq.heappop(self.firsthalf)
                heapq.heappush(self.secondhalf, -largest)
                print(f"1st half reshuffling. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
        
        if self.currLen % 2:
            print(f"Odd median calculation. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
            if len(self.firsthalf) > len(self.secondhalf):
                self.currMedian = -self.firsthalf[0]
                print(f"1st half median selected: {self.currMedian}")
            else:
                self.currMedian = self.secondhalf[0]
                print(f"2nd half median selected: {self.currMedian}")
        else:
            print(f"Even median calculation. Current first half: {self.firsthalf}, current second half: {self.secondhalf}")
            self.currMedian = (-self.firsthalf[0] + self.secondhalf[0]) / 2
            print(f"Median selected: {self.currMedian}")
        return

    def findMedian(self) -> float:
        return self.currMedian