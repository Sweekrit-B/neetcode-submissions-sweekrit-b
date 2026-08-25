class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm
        # cut principle - at any given point, you need to connect the values NOT in the tree to the values in the tree. the cheapest edge spanning the two groups MUST be part of the MST, because if it is not, then there must be a more expensive way to go around
        # therefore, at every point, you greedily take the cheapest option

        # this problem is prim's 
            # nodes are the different points
            # edges are the manhattan distance to the points
        
        # start with creating an adjacency list with weights
        points_set = points
        adj_list = defaultdict(list)

        for i in points:
            for j in points:
                adj_list[tuple(i)].append((
                    abs(i[0] - j[0]) + abs(i[1] - j[1]),
                    (j[0], j[1])
                ))
        
        # create a visited set
        visited = set()
        min_heap = [(0, tuple(points[0]))] # the first point has weight 0
        total_cost = 0

        # while the heap is still present and we have visited less than the appropriate amount of items (i.e. while we still have edges to iterate through)
        while min_heap and len(visited) < len(points):
            weight, point = heapq.heappop(min_heap)
            if point in visited:
                continue # we have already considered the shortest connection
            
            total_cost += weight
            visited.add(point)

            for neighbor in adj_list[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, neighbor)
        
        return total_cost
