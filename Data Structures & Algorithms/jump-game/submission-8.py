class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dynamic programming solution
        if len(nums) == 1:
            return True
        
        can_next_T = [False] * (len(nums)-1)
        can_next_T[-1] = True
        next_T = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= next_T:
                can_next_T[i] = True
                next_T = i
            else:
                can_next_T[i] = False
        
        return can_next_T[0]

        