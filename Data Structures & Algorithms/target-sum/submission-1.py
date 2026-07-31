class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(val, level):
            # print(f"Level {level}, looking at {val}")
            if val == 0 and level == len(nums):
                # print(f"Found a valid sequence, bubbling back up")
                return 1
            if val != 0 and level == len(nums):
                # print("Found an invalid sequence, bubbling back up")
                return 0

            num = nums[level]
            # print(f"Number of interest: {num}")
            branch_1_root = val - num
            # print(f"Branch 1 root: {branch_1_root}")
            branch_2_root = val + num
            # print(f"Branch 2 root: {branch_2_root}")

            cache[(branch_1_root, level + 1)] = dfs(branch_1_root, level + 1)
            # print(f"Value of DFS of branch 1: {cache[(branch_1_root, level + 1)]}")
            cache[(branch_2_root, level + 1)] = dfs(branch_2_root, level + 1)
            # print(f"Value of DFS of branch 2: {cache[(branch_2_root, level + 1)]}")

            cache[(val, level)] = cache[(branch_1_root, level + 1)] + cache[(branch_2_root, level + 1)]
            # print(f"Final DFS: {cache[(val, level)]}")
            return cache[(val, level)]
        
        return dfs(target, 0)