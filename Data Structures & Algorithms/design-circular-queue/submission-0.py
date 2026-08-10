class MyCircularQueue:
    # idea: use a two pointer system
        # initialize:
            # array of size k
            # front pointer @ index 0
            # rear pointer @ index 0
        # Front() -> return array[front]
        # Rear () -> return array[rear]
        # enQueue
            # array[rear pointer] = value that we are adding
            # rear pointer += 1 (must do mod len(arr))
        # deQueue
            # array[front pointer] = None
            # front pointer += 1 (must do mod len(arr))
        # isEmpty() -> if front pointer == rear pointer and array[front pointer] = None
        # isFull() -> if front pointer == rear pointer and array[front pointer] != None

    def __init__(self, k: int):
        self.arr = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.arr[self.rear] == None:
            self.arr[self.rear] = value
            self.rear = (self.rear + 1) % len(self.arr)
            # print(f"Was able to enqueue: {self.arr}, front & rear: {self.front, self.rear}")
            return True
        else:
            # print(f"Was not able to enqueue: {self.arr}, front & rear: {self.front, self.rear}")
            return False

    def deQueue(self) -> bool:
        if self.arr[self.front] != None:
            self.arr[self.front] = None
            self.front = (self.front + 1) % len(self.arr)
            # print(f"Was able to dequeue: {self.arr}, front & rear: {self.front, self.rear}")
            return True
        else:
            # print(f"Was not able to dequeue: {self.arr}, front & rear: {self.front, self.rear}")
            return False

    def Front(self) -> int:
        # print(f"Trying to find front value at index {self.front} in {self.arr}")
        return self.arr[self.front] if self.arr[self.front] != None else -1

    def Rear(self) -> int:
        # print(f"Trying to find rear value at index {self.rear - 1} in {self.arr}")
        return self.arr[self.rear-1] if self.arr[self.rear-1] != None else -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.arr[self.front] == None

    def isFull(self) -> bool:
        return self.front == self.rear and self.arr[self.front] != None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()