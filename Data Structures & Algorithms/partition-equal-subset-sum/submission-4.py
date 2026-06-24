class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # inefficient solution - recursive 2^n
        overall_sum = sum(nums)
        if overall_sum % 2 == 1:
            return False
        possible_starts = set()
        for num in nums:
            # print(f"looking at {num}, here are possible starts: {possible_starts}")
            if num == (overall_sum // 2):
                return True
            to_add = []
            for start in possible_starts:
                curSum = start + num
                # print(f"Got {curSum} by doing {start} plus {num}")
                if curSum == (overall_sum // 2):
                    return True
                if curSum < (overall_sum // 2):
                    to_add.append(curSum)
            for val in to_add:
                possible_starts.add(val)
            possible_starts.add(num)
        # print(possible_starts)
        return False