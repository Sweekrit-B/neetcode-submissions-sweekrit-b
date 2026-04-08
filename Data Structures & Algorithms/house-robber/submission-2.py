class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        money_robbed = [0] * n

        money_robbed[0] = nums[0]
        money_robbed[1] = nums[1]

        temp_max = max(nums[0], nums[1])
        curr_max = nums[0]

        for i in range(2, n):
            # print("At index ", i, " with current max as ", curr_max, " and temp max as ", temp_max)
            money_robbed[i] = nums[i] + curr_max
            if temp_max > curr_max:
                curr_max = temp_max
            if money_robbed[i] > curr_max:
                temp_max = money_robbed[i]
        
        # print(money_robbed)
        return max(money_robbed[-2], money_robbed[-1])
