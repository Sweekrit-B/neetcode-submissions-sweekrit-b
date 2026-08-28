class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # start by sorting the array so we have clear ranking
        # [1, 2, 4, 5], limit = 6
        # how do we now determine fitting under the limit?
            #  l = 0, r = 3
                # here, since l and r combine to equal 6, we can add them as a pair
                # we can also do l += 1 and r -= 1
                # 4 and 2 then follow the same pattern
        
        # now, lets say we had 
        # [1, 2, 3, 4], limit = 6
            # l = 0, r = 3
                # here, however, when we check l and r, we notice its LESS than 6
                # therefore, we move l forward -> l = 1, r = 3
                # now, the values are equal, therefore we add the pair
                # next, we move both values -> l += 1 and r -= 1 -> they land at 2
                # a unique thing that we notice is that BECAUSE we have already dealt with the largest possible values and added them in, everything REMAINING can just be paired up!
        
        # finally, lets say we had
        # [2, 2, 3, 4], limit = 5
            # l = 0, r = 3
                # here, the sum is too large
                # therefore, we know that there is no value small enough to ensure that 4 is paired with someone, so we put them in their own boat
                # then, we do r -= 1, and add an individual boat
        
        people.sort()
        skipped_people, num_boats = 0, 0
        l, r = 0, len(people)-1

        while l < r:
            if people[l] + people[r] > limit:
                num_boats += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                if people[l] != people[l + 1] and people[l + 1] + people[r] <= limit:
                    l += 1
                    skipped_people += 1
                else:
                    l += 1
                    r -= 1
                    num_boats += 1
        
        if l == r: skipped_people += 1
        num_boats += -(-skipped_people // 2)
        return num_boats