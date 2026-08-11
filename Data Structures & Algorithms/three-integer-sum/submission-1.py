class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # extra challenge: let's try to get a general n sum solution
        # core idea: we are defining a recursive algorithm
        # sum(n, start_ix, target)
            # n = number of sums that we have left
            # start_ix = start index for that specific sum
            # target = the target value for the remaining sum
        # first, sort the array
        # each time we call sum, we do the following:
            # 1) if this is a 2sum, then:
                # do the two pointer method to find values that fit
                # return a list of those values
            # 2) if this is >2 sum, then:
                # sums: []
                # for each i in range(start_ix, len(nums) - n + 1):
                    # if i > start_ix and nums[i] == nums[i-1]:
                        # continue --> skip this value because we have already checked this one
                    # else:
                        # for result from sum(n-1, start_ix+1, target - nums[i]):
                            # possible_sums.append(nums[i] + result)
                # return those sums
            # at the end, you should have a list of everything
        
        nums = sorted(nums)

        def two_sum(arr, target):
            l, r = 0, len(arr)-1
            sums = set()
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
                        continue # this value has already been checked
                    else:
                        for sum_arr in find_sum(n-1, ix + 1, target - nums[ix]):
                            sums.add(tuple(sorted([nums[ix]] + list(sum_arr))))
                return sums
        
        all_sums = find_sum(3, 0, 0)
        res = []
        for each_sum in all_sums:
            res.append(list(each_sum))
        
        return res