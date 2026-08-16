class Solution:
    def jump(self, nums: List[int]) -> int:
        # initial idea - n^k solution where n is the number of steps and k is the potential number of options at each step
        # we can use memoization to decrease this

        cache = {}

        def dfs(step_ix):
            if step_ix >= len(nums)-1:
                # reached the end, minimum jumps from this point is 0
                cache[step_ix] = 0
                return 0 
            if step_ix in cache:
                # we have already seen this value before, return the minimum cached value
                return cache[step_ix]
            if nums[step_ix] == 0:
                # if we literally cannot progress foward
                cache[step_ix] = float('inf')
                return float('inf')

            min_jumps = min([1 + dfs(step_ix + num_jumps) for num_jumps in range(1, nums[step_ix]+1)])
            cache[step_ix] = min_jumps
            return min_jumps
        
        return dfs(0)