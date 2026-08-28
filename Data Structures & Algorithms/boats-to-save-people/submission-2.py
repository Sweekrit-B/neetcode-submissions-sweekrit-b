class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # just carry the heaviest person and the lightest person
        # don't have to skip anything

        people.sort()
        num_boats = 0
        l, r = 0, len(people)-1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            num_boats += 1
            if l <= r and remain >= people[l]:
                l += 1
        
        return num_boats