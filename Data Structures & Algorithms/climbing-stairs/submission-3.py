class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 4
        # no. of ways to climb 0 stairs - 1
        # no. of ways to climb 1 stair - 1
        # no. of ways to climb 2 stairs - 2
        # no. of ways to climb 3 stairs - no. of ways to climb 3-1 stairs + no. of ways to climb 3-2 stairs = 3
        
        arr = [1, 1] # no. of ways to climb 0 and 1 stairs
        while len(arr) <= n:
            arr.append(arr[-2] + arr[-1])
        return arr[-1]
