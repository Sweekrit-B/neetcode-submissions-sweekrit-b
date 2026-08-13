class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i, num in enumerate(nums):
            if target-num not in seen_nums:
                seen_nums[num] = i
            else:
                return [seen_nums[target-num], i]
