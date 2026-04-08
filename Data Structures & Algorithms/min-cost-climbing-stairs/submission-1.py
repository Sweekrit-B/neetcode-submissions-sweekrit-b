class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minTwoAway, minOneAway = 0, 0

        for i in range(2, len(cost)+1):
            newCost = min(minTwoAway + cost[i-2], minOneAway + cost[i-1])
            minTwoAway, minOneAway = minOneAway, newCost

        return minOneAway