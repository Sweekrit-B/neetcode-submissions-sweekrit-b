class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # general solution: recurse downward until you get to two sum
        nums.sort()

        def two_sum(arr, target):
            sums = set()
            l, r = 0, len(arr)-1
            while l < r:
                if arr[l] + arr[r] > target:
                    r -= 1
                elif arr[l] + arr[r] < target:
                    l += 1
                else:
                    sums.add(tuple(sorted([arr[l], arr[r]])))
                    l += 1
                    r -= 1
            return sums
        
        def find_sum(n, start_ix, target):
            if n == 2:
                return two_sum(nums[start_ix:], target)
            else:
                sums = set()
                for ix in range(start_ix, len(nums) - n + 1):
                    if ix > start_ix and nums[ix] == nums[ix - 1]:
                        continue
                    else:
                        for sum_arr in find_sum(n-1, ix + 1, target - nums[ix]):
                            sums.add(tuple(sorted([nums[ix]] + list(sum_arr))))
            return sums
        
        all_sums = find_sum(4, 0, target)
        res = []
        for sum_tup in all_sums:
            res.append(list(sum_tup))
        
        return res