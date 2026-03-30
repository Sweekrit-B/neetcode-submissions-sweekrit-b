class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_list = set()
        all_sets = []
        
        def dfs(arr, curr_index):
            # print("Next iteration")
            # print("Array: ", arr)
            # print("Sorted array: ", sorted(arr))
            if arr: # in the normal case
                tup_arr = tuple(sorted(arr)) # make an array out of the list for set addition
                if tup_arr not in subset_list: # if we have not already explored this path...
                    # print("Unique value found, adding...")
                    subset_list.add(tuple(sorted(arr))) # add the value to the subset list
                    # print(subset_list)
            if not arr: # in the empty case
                subset_list.add(()) # add an empty tuple
                # print("Unique value found, adding...")
                # print(subset_list)
            
            for i in range(curr_index, len(nums)):
                dfs(arr + [nums[i]], i+1)
        
        dfs([], 0)

        for tup in subset_list:
            all_sets.append(list(tup))

        # print(subset_list)
        # print(all_sets)
        return all_sets

            