class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sets = set()
        min_num = min(candidates)

        def dfs(arr, val, choices):
            if val == 0:
                sets.add(tuple(sorted(arr)))
                return
            if val < min_num or not choices:
                return
            for num in choices:
                choices_copy = choices.copy()
                choices_copy.remove(num)
                dfs(arr + [num], val - num, choices_copy)
        
        dfs([], target, candidates)

        output_sets = []
        for subset in sets:
            output_sets.append(list(subset))

        return output_sets