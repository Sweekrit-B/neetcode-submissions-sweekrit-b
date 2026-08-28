class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # fixed size sliding window
        # for each window, check the overall distance
        # return the window with the least distance

        def find_dist_from_x(l, r):
            dist = 0
            res_arr = []
            for i in range(l, r):
                dist += abs(arr[i] - x)
                res_arr.append(arr[i])
            return dist, res_arr

        l, r = 0, k
        min_dist = float('inf')
        res = []
        while r <= len(arr):
            curr_dist, curr_res_arr = find_dist_from_x(l, r)
            if curr_dist < min_dist:
                min_dist = curr_dist
                res = curr_res_arr
            l += 1
            r += 1
        return res