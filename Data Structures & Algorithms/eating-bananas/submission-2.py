import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pattern: doing binary search on a solution --> O(n log n) solution
        # step 1: define a function to check how many hours to eat all the bananas
        # step 2: do a binary search on that solution

        def hours_taken(eating_rate):
            return sum([math.ceil(pile / eating_rate) for pile in piles])
        
        l = 1
        r = max(piles) # at this rate, you get the minimum hours taken, which is len(piles)

        while l < r:
            m = ((l + r) // 2)
            if hours_taken(m) <= h: # if the bananas CAN be eaten in this timeframe
                r = m # move r to m, as now we need to check the left side
            else:
                l = m+1 # move l to m+1, as we know that m does not work, and we need to check the right side

        return l

        # l = 0, r = 4
        # m = 2, hours_taken(2) = 6, 6 <= 9 --> look at left side
        # l = 0, r = 2
        # m = 1, hours_taken(1) = 10, 10 > 9 --> look at right side
        # l = 2, r = 2
        # l < r is no longer true, return l