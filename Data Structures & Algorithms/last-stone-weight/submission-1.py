class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using a max heap...
        # step 1: pop the biggest stone
        # step 2: pop the next biggest stone
        # step 3: smash the stones together
        # step 4: pop any remaining stones back
        # step 5: repeat this process until there is only one stone left
        # step 6: return the weight of that stone

        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            biggest = -heapq.heappop(stones)
            second_biggest = -heapq.heappop(stones)
            print(f"Biggest: {biggest}, second biggest: {second_biggest}")
            if biggest == second_biggest:
                continue
            if biggest > second_biggest:
                new_weight = biggest - second_biggest
                print(f"New weight: {new_weight}")
                heapq.heappush(stones, -new_weight)
                print(f"Added new weight to {stones}")
        return 0 if not stones else -stones[0]