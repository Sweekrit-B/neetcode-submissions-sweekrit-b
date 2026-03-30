class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sets = set()

        def dfs(arr, choices):
            if len(arr) == len(nums):
                sets.add(tuple(arr))
            for val in choices:
                choices_copy = choices.copy()
                choices_copy.remove(val)
                dfs(arr + [val], choices_copy)
        
        dfs([], nums)

        output_sets = []
        for subset in sets:
            output_sets.append(list(subset))
        
        return output_sets