class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            res = float('inf')
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    res = min(res, 1 + dp[i - coin])
            dp[i] = res
        
        ans = dp[-1]
        return ans if ans != float('inf') else -1