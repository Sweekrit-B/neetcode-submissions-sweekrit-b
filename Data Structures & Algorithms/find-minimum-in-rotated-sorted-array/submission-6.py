class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 6, 1, 2]
        # finding the minimum in log n time = clue for binary search
        # start with left pointer (l = start) and right pointer (r = end)
        # key point is that due to the rotation
            # if our middle value is greater than our right value OR middle value is less than left
                # the minimum is in the right side
                # this is because the cycle should occur between the middle and the right
            # the opposite also applies - if the middle value is less than our right value OR the middle value is greater than the left
                # the minimum is on the left side
        
        # dry run
        # compare m to r because m will always round down, so they will never be equal until there is only one value left
        # [3 (l), 4, 5, 6, 1, 2 (r)] -> l = 0, r = 5, m = 2
            # [3 (l), 4, 5 (m), 6, 1, 2 (r)] -> m > r --> therefore, it must be right side
            # l = m + 1
        # [6 (l), 1 (m), 2 (r)] -> m < r --> therefore, it must be the left side
            # r = m
        # [6 (l), 1 (r)] -> m > r --> therefore, must be right side
            # l = m + 1
        # [1]

        l, r = 0, len(nums)-1
        while l < r:
            # if nums[l] < nums[r]:
            #     return nums[l]
            m = (l + r)//2
            if nums[m] > nums[r]:
                # must be on the right side
                l = m + 1
            else:
                r = m
        return nums[l]