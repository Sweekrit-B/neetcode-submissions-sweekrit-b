class Solution:
     def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))

        def dp(arr):
            rob_arr = arr[:2]
            unallowed = 0
            max_rob = 0

            for i in range(2, len(arr)):
                unallowed += 1
                max_rob = max(max_rob, rob_arr[unallowed - 1])
                rob_arr.append(max_rob + arr[i])
            
            return max(rob_arr)

        inclusive_dp = dp(nums[:-1])
        exclusive_dp = dp(nums[1:])
        return max(inclusive_dp, exclusive_dp)