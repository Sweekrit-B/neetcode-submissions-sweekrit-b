class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_list = set() # O(2n) = O(n) is space complexity
        all_sets = []
        
        def dfs(arr, curr_index): # O(n^4 log n) is time complexity
            if arr: # in the normal case
                tup_arr = tuple(sorted(arr)) # make an array out of the list for set addition -> O(n log n)
                if tup_arr not in subset_list: # if we have not already explored this path... -> O(1)
                    subset_list.add(tuple(sorted(arr))) # add the value to the subset list
            if not arr: # in the empty case
                subset_list.add(()) # add an empty tuple 
            
            for i in range(curr_index, len(nums)):
                dfs(arr + [nums[i]], i+1) # amount of DFS calls = n(n^2 - 1)/6 = O(n^3)
        
        dfs([], 0)

        for tup in subset_list:
            all_sets.append(list(tup))

        return all_sets

            