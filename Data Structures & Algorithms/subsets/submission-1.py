class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # neetcode
        res = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            subsets.append(nums[i]) # add the value to the subset
            dfs(i + 1) # run DFS and add all subsets with this value
            subsets.pop()
            dfs(i + 1) # run DFS and add all subsets without this value
    
        dfs(0)
        return res
