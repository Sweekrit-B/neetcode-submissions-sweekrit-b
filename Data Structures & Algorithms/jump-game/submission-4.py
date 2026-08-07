class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # observations:
            # if you get to a postition at which nums[i] == 0, you can't move on from there
            # ideally, you want to jump your maximum length each time
                # each time you don't make it, you backtrack
        
        # backtracking solution
        # start with pos = [0]
        # make the first jump -> pos = [0, 1]
        # make the second jump (2) -> pos = [0, 1, 3]
            # nums 3 == 0
            # pop the pos value
            # make the jump from 2-1 = 1 -> pos = [0, 1, 2]
        # make the third jump (3) -> pos = [0, 1, 2, 3]
            # nums 3 == 0
            # pop the pos value
            # cannot make any more jumps

        pos = [0]
        t = 1

        while pos[-1] < len(nums) - 1: # once pos is at that, we can reach the goal
            jump_val = nums[pos[-1]] # how much can you jump at this point
            # print(f"Currently, can jump: {jump_val}")
            while jump_val == 0:
                pos.pop()
                # print(f"Updating pos: {pos}")
                if not pos:
                    return False
                nums[pos[-1]] -= 1
                jump_val = nums[pos[-1]]
                # print(f"Updating nums: {nums}")
                # print(f"Updating jump val: {jump_val}")
            next_pos = pos[-1] + jump_val
            # print(f"Got next position: {next_pos}")
            pos.append(next_pos)
            # print(f"Updating pos: {pos}")
        
        return True


            

            