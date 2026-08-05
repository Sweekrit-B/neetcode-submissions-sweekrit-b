class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def find_max_and_num_maxes(arr):
            val_counts = defaultdict(int)
            for val in arr:
                val_counts[val] += 1
            max_val = max(arr)
            return max_val, val_counts[max_val]
        
        curr_max, num_maxes = find_max_and_num_maxes(nums[:k])
        max_arr = [curr_max]
        print(f"Initial: {curr_max, num_maxes}")
        l, r = 0, k

        while r < len(nums):
            # iterate r forward to add the new item
            new_val = nums[r]
            # print(f"Considering: {new_val}")
            if new_val > curr_max:
                curr_max = new_val
                num_maxes = 1
                # print(f"Found a new maximum: {curr_max, num_maxes}")
            elif new_val == curr_max:
                num_maxes += 1
                # print(f"Found the same maximum: {curr_max, num_maxes}")
            r += 1
            # print(f"Intermediarily considering range {nums[l:r]}")
            # iterate l forward to remove the last item
            removed_val = nums[l]
            if removed_val == curr_max:
                num_maxes -= 1
                # print(f"Removed a maximum: {curr_max, num_maxes}")
            l += 1
            # print(f"Finally considering range {nums[l:r]}")
            if num_maxes == 0:
                curr_max, num_maxes = find_max_and_num_maxes(nums[l:r])
                # print(f"Found a new maximum: {curr_max, num_maxes}")
            # add the finalized current maximum to the array
            # print(f"Final maximum: {curr_max, num_maxes}")
            max_arr.append(curr_max)
        
        return max_arr
