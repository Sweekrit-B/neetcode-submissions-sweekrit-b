"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start with [(0, 40), (5, 10), (15, 20)]
            # we want to not merge any intervals
        # sort all intervals by start value
        # for each interval -> if end of interval is less than next start value, merge them together

        if not intervals:
            return 0

        intervals = sorted(intervals, key = lambda interval: interval.start)
        min_heap = [intervals[0].end]
        # print(f"Original heap: {min_heap}")

        for i in range(1, len(intervals)):
            # print(f"Intervals: {intervals[i].start, intervals[i].end}")
            if min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, intervals[i].end)
                # print(f"New heap: {min_heap}")
            else:
                heapq.heappush(min_heap, intervals[i].end)
        
        return len(min_heap)