class Solution:
     def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))

        def dp(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))