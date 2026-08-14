class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot point (i.e. the min value)
        l, r = 0, len(nums)-1
        while l < r:
            m = ((l + r) // 2)
            # print(f"Left: {l}, right: {r}, mid: {m}")
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        min_ix = l
        # print(f"Found minimum index {min_ix} with value {nums[min_ix]}")

        # determine if the target is greater than the leftmost value
            # if it is, then we search from l to min_ix - 1
            # if it is not, we search from min_ix to r
        
        def binary_search(l, r):
            nonlocal target
            nonlocal nums

            while l < r:
                m = ((l + r) // 2)
                # print(f"Left: {l}, right: {r}, mid: {m}")
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
            
            return l if nums[l] == target else -1
        
        if target >= nums[min_ix] and target <= nums[-1]:
            return binary_search(min_ix, len(nums) - 1)
        else:
            return binary_search(0, min_ix - 1)