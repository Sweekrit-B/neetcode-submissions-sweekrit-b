class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minTwoAway, minOneAway = 0, 0
        floorTwoAway, floorOneAway = 0, 1
        while floorOneAway < len(cost):
            tempCost = minTwoAway
            minTwoAway = minOneAway # new minTwoAway becomes current minOneAway
            minOneAway = min(tempCost + cost[floorTwoAway], minOneAway + cost[floorOneAway])

            floorTwoAway += 1
            floorOneAway += 1
        return minOneAway