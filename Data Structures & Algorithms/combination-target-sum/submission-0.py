class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sets = set()
        min_num = min(nums)

        def dfs(arr, val):
            if val == 0:
                sets.add(tuple(sorted(arr)))
                return
            if val < min_num:
                return
            for num in nums:
                dfs(arr + [num], val - num)
        
        dfs([], target)

        output_sets = []
        for subset in sets:
            output_sets.append(list(subset))

        return output_sets

        