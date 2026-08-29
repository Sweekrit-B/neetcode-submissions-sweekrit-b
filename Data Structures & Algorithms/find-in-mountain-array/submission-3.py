class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # we have to use binary search, but how?
        # observations:
            # if we know the peak, it's trivial to run binary search on both sides of the mountain to get our result
            # how do we find the peak?
                # find mid, and then [mid - 1, mid, mid + 1]
                # if mid - 1 < mid < mid + 1 -> you are on the left side, l = m + 1
                # if mid - 1 > mid > mid + 1 -> you are on the right side, r = m - 1
                # if mid -1 < mid and mid > mid + 1 -> you are at the peak!
        
        # [1, 10, 9, 8, 7], target = 8
        # find peak -> l = 0, r = 4
            # m = 2
                # prev = 10, mid = 9, nxt = 8
                # l = 0, r = 1
            # m = 0
                # prev = 1, mid = 1, nxt = 10
                # l = 1, r = 1
        
        n = mountainArr.length()

        def find_peak():
            l, r = 0, n-1
            while l <= r:
                m = (l + r) // 2
                prev = float('-inf') if m == 0 else mountainArr.get(m-1)
                mid = mountainArr.get(m)
                nxt = float('inf') if m == n-1 else mountainArr.get(m+1)
                if prev <= mid < nxt:
                    l = m + 1
                elif prev > mid > nxt:
                    r = m - 1
                elif prev < mid and mid > nxt:
                    return m
        
        def search_left(p):
            l, r = 0, p
            while l <= r:
                m = (l + r) // 2
                mid = mountainArr.get(m)
                if mid == target: return m
                if mid < target: l = m + 1
                if mid > target: r = m - 1
            return -1
        
        def search_right(p):
            l, r = p, n-1
            while l <= r:
                m = (l + r) // 2
                mid = mountainArr.get(m)
                if mid == target: return m
                if mid < target: r = m - 1
                if mid > target: l = m + 1
            return -1

        peak = find_peak()
        left = search_left(peak)
        right = search_right(peak)

        return right if left == -1 else left