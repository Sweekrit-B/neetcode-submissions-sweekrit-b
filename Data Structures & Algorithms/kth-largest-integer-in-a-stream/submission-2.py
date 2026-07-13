class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create a min heap with nums
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        # print(f"Initial nums: {self.nums}")
        heapq.heappush(self.nums, val)
        # print(f"New nums: {self.nums}")
        while len(self.nums) > self.k:
            # print("Nums is too big! Popping the minimum")
            heapq.heappop(self.nums)
            # print(f"Nums after popping: {self.nums}")
        # print(f"Final heap: {self.nums}")
        heapq.heapify(self.nums)
        # print(f"Heapified nums: {self.nums}")
        return self.nums[0]
        
