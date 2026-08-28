class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # move right pointer forward until sum is greater than
        # then move left pointer to minimize size as much as possible
        # repeat this process until the end of the array

        l, r = 0, 0
        curr_sum = 0
        res = float('inf')
        while r < len(nums):
            curr_sum += nums[r]
            # print(f"Sum after adding r ({nums[r]}): {curr_sum}")
            if curr_sum >= target:
                res = min(res, r - l + 1)
                # print(f"New result: {res}")
                while curr_sum - nums[l] >= target:
                    # print(f"We can reduce the size!")
                    curr_sum -= nums[l]
                    l += 1
                    # print(f"New left value at l ({nums[l]}); current sum: {curr_sum}")
                    res = min(res, r - l + 1)
                    # print(f"New result: {res}")
            r += 1
        return 0 if res == float('inf') else res