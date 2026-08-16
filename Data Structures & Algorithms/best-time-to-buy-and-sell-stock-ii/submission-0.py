class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # trick: you are optimally buying and selling. Therefore, you want to simply calculate the sum of all the increasing slopes
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res