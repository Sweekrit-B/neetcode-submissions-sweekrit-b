class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sets = []
        def dfs(arr):
            if arr:
                arr = sorted(arr) # O(n log n)
                sets.append(arr)
                greater_than_nums = [num for num in nums if num > arr[-1]]
            else:
                sets.append(arr)
                greater_than_nums = nums

            for num in greater_than_nums: # O(n)
                dfs(arr + [num])
        dfs([])
        return sets

        