class Solution:
    def rob(self, nums: List[int]) -> int:
        # at any given point, you are allowed to rob the house not right before you
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = [nums[0], max(nums[0], nums[1])] # max you can rob before this point
        for i in range(2, len(nums)):
            res.append(max(res[-1], (res[-2] + nums[i])))
        print(res)
        return max(res)