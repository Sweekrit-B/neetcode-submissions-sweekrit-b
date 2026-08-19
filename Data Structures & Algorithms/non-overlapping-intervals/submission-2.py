class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # as we go through, anything that overlaps, don't include
        intervals.sort()
        print(intervals)
        non_overlapping_intervals = []
        res = 0
        for interval in intervals:
            # print(f"Current interval: {interval}, current non overlapping: {non_overlapping_intervals}, current res: {res}")
            if not non_overlapping_intervals:
                non_overlapping_intervals.append(interval)
                continue
            # if interval is overlapping, skip
            last_added = non_overlapping_intervals[-1]
            if last_added[1] > interval[0]:
                res += 1
                if interval[1] < last_added[1]:
                    non_overlapping_intervals[-1] = interval
            # if not overlapping, add
            else:
                non_overlapping_intervals.append(interval)
        
        return res
