class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # neetcode
        # Bellman Ford algorithm
            # after k + 1 layers of BFS, what is the minimum cost?
            # keep a temporary prices array
            # go through every edge in the graph and update a temporary prices array
                # i.e. take the source value + edge weight = end value
                # you're only going to be able to update prices you can reach at that layer, otherwise it will be infinity
            # we get the smallest price to reach each node after ONE layer

        prices = [float('inf')] * n
        prices[src] = 0 

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'): # cannot reach this source node
                    continue
                if prices[s] + p < tmpPrices[d]: # get minimum value at the layer
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]
        
