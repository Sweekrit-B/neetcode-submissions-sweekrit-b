class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # hint solution
        lis = [0] * len(nums)
        lis[-1] = 1
        for i in range(len(nums) - 1, -1, -1):
            lis_vals = []
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    lis_vals.append(lis[j])
            lis[i] = 1 if not lis_vals else (max(lis_vals) + 1)
        
        return max(lis)