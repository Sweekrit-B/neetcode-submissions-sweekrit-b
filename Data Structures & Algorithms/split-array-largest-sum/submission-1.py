class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # this is similar to koko eating bananas and the ship problem?
        # core question: how do you determine, given a value x, that the array can be split into k components such that x is the largest?
            # start at 0 -> continue until u cannot add a value -> thats a new subarray
            # if there are too many subarrays, that means the value can increase
            # if there are too few or just enough subarrays, it means the value can decrease
        
        # cannot use a greedy approach 
        def find_amt_subarrays_for_sum(x):
            curr_sum = 0
            curr_subarrays = 0
            for num in nums:
                if curr_sum + num > x:
                    curr_subarrays += 1
                    curr_sum =0
                curr_sum += num
            return curr_subarrays + 1
        
        # print(find_amt_subarrays_for_sum(16))

        best_x = sum(nums)
        l, r = max(nums), sum(nums)
        while l <= r:
            m = (l + r) // 2
            min_possible_subarrays = find_amt_subarrays_for_sum(m)
            print(f"Amount of subarrays for this midpoint {m}: {min_possible_subarrays}")
            if min_possible_subarrays <= k:
                # we can get k or less subarrays
                best_x = min(m, best_x)
                r = m - 1
            else:
                # we can get more than k subarrays
                l = m + 1
        
        return best_x