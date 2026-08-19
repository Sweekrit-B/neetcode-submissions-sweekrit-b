class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged_intervals = []

        for ix, interval in enumerate(intervals):
            if not merged_intervals:
                merged_intervals.append(interval)
                continue
            last_added = merged_intervals[-1]
            if interval[0] > last_added[1]:
                merged_intervals.append(interval)
            else:
                new_min = min(interval[0], last_added[0])
                new_max = max(interval[1], last_added[1])
                merged_intervals[-1] = [new_min, new_max]
        
        return merged_intervals