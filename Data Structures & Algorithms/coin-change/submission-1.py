class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        # for coin in coins:
        #     dp[coin] = 1
        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if amt in dp:
                return dp[amt]
            
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(amt - coin))
            dp[amt] = res
            return res
        ans = dfs(amount)
        return ans if ans != float('inf') else -1