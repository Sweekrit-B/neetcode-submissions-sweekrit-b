class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dumb solution? if a value is 0, the next value must be big enough to clear it
        i = len(nums) - 2
        necessary_jump_to_clear = None
        while i >= 0:
            # print(f"At index {i}, value {nums[i]}")
            if necessary_jump_to_clear:
                if nums[i] >= necessary_jump_to_clear:
                    # print(f"Current index {i} can clear, resetting")
                    necessary_jump_to_clear = None
                else:
                    necessary_jump_to_clear += 1
                    # print(f"Adding to the necessary jump to clear: {necessary_jump_to_clear}")
            elif nums[i] == 0:
                necessary_jump_to_clear = 2
                # print(f"Need to jump {necessary_jump_to_clear} to clear index {i}")
            i -= 1
        return not necessary_jump_to_clear