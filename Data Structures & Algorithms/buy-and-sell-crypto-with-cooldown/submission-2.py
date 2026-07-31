class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_list = [0]*(n+2)
        sell_list = [0]*(n+2)

        for price_ix in range(len(prices) - 1, -1, -1):
            buy_list[price_ix] = max(-prices[price_ix] + max(sell_list[price_ix+1:]), max(buy_list[price_ix+1:]))
            sell_list[price_ix] = max(prices[price_ix] + max(buy_list[price_ix+2:]), max(sell_list[price_ix+1:]))
        
        return buy_list[0]