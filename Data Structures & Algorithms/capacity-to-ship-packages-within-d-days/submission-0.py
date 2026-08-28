class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # problem seems similar to koko eating bananas
        # find the minimum value such that the amount of time it takes to ship packages is less than or equal to "days" variable

        # subproblem: how to efficiently determine how many days it will take to ship packages with a certain weight capacity?
        # store the amount of days & current accumulated weight
        # when current accumulated + new weight > limit -> add 1 to days and reset current accumulated = new weight
        # continue until you reach the end

        def days_for_limit(limit):
            curr_acc_weight, days = 0, 0
            for weight in weights:
                # print(f"Measuring weight: {weight}")
                if curr_acc_weight + weight > limit:
                    # print(f"Over the limit! Adding one more day: {days+1}")
                    days += 1
                    curr_acc_weight = 0
                curr_acc_weight += weight
                # print(f"New current weight: {curr_acc_weight}")
            return days + 1 # add 1 for the remaining current weight
        
        # binary search to find the least weight where days is below the bar
        # find a midpoint m
            # if the amount of days taken is less than or equal to the limit, move r to m
                # m can still technically be the answer
            # if the amount of days taken is greater than the limit, move l to m+1

        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if days_for_limit(m) > days:
                l = m + 1
            else:
                r = m
        
        return r