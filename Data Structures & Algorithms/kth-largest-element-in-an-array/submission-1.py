import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        # print(heap)
        for i in range(k-1):
            heapq.heappop(heap)
            # print(heap)
        return -heapq.heappop(heap)