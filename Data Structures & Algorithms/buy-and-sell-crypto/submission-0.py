class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 1, 5, 6, 7, 1]
        # b = 0, s = 0 -> profit = 0 -> move from b, s 10 to 1
        # since 1 <= 10, b = 1, s = 1 -> profit = 0 -> move s from 1 to 5
        # since 5 > 1, b = 1, s = 2 -> profit = 4 -> move s from 5 to 6
        # since 6 > 1, b = 1, s = 3 -> profit = 5 -> move s from 6 to 7
        # since 7 > 1, b = 1, s = 4 -> profit = 6 -> move b, s from 7 to 1
        # since 1 <= 1, b = 5, s = 5 -> profit = 0

        # sliding window/two pointers
        # if the current price is less than or equal to prices[b], move b & s to the current price
        # if the current price is greater than prices[b], just move s and record the max profit

        maxProfit = 0
        b, s = 0, 0
        for i in range(len(prices)):
            if prices[s] > prices[b]:
                maxProfit = max(maxProfit, prices[s]-prices[b])
            else:
                b = s
            s += 1
        return maxProfit