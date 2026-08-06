class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # old solution
        nums = sorted(nums)
        sets = []
        def dfs(arr):
            if arr:
                arr = sorted(arr)
                sets.append(arr)
                greater_than = [num for num in nums if num > arr[-1]]
            else:
                sets.append(arr)
                greater_than = nums
            
            for num in greater_than:
                dfs(arr + [num])
        
        dfs([])
        return sets