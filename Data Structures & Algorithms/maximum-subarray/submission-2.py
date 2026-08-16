class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy approach
        # idea - at any given point, evaluate whether extending the sum or starting fresh would be better
            # to do this, compare the current value to current value + current sum
            # if current value > current value + current sum, then start fresh

        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            # print(f"Considering {num} with current sum {curr_sum}")
            if num > curr_sum + num:
                curr_sum = num
                # print(f"Better to start fresh from {num}")
            else:
                curr_sum += num
                # print(f"Adding to the current sum to get {curr_sum}")
            max_sum = max(max_sum, curr_sum)
        
        return max_sum