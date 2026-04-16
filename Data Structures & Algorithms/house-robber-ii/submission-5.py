class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))

        def dp(arr, initial_arr):
            rob_arr = initial_arr
            max_rob = 0
            unallowed = 0
            for i in range(2, len(arr)):
                unallowed += 1
                max_rob = max(max_rob, rob_arr[unallowed - 1])
                rob_arr.append(max_rob + arr[i])
            return rob_arr


        exclude = [0, nums[1]] # exclusive array w/o first val
        include = nums[0:2] # inclusive array w/ first val
       
        return max(dp(nums, exclude)[-1:] + dp(nums, include)[:-1])