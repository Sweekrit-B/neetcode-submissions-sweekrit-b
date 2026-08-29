class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # neetcode
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target: return True

            if nums[l] < nums[m]: # left portion (i.e. the MIDDLE is in the LEFT sorted portion)
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]: # right portion (i.e. the MIDDLE is in the RIGHT sorted portion)
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # cannot determine which portion we are in
                l += 1
        
        return False