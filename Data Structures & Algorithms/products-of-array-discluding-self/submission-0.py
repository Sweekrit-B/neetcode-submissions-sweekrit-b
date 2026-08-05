class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = [1]
        suffix_prods = [1]

        for i in range(1, len(nums)):
            prefix_prods.append(prefix_prods[-1] * nums[i-1])

        for i in range(len(nums) - 2, -1, -1):
            suffix_prods.append(suffix_prods[-1] * nums[i+1])
        
        suffix_prods = suffix_prods[::-1]

        res = []
        for i in range(len(prefix_prods)):
            res.append(prefix_prods[i] * suffix_prods[i])
        
        return res