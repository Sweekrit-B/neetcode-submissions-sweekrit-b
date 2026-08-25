class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal's algorithm - uses sorted edges and a disjoint set
        edges = []
        
        for i_idx in range(len(points)):
            for j_idx in range(i_idx+1, len(points)):
                i = tuple(points[i_idx])
                j = tuple(points[j_idx])
                distance = abs(i[0] - j[0]) + (abs(i[1] - j[1]))
                edges.append((i, j, distance))

        # define kruskal's algorithm
        def kruskals(edges):
            edges.sort(key=lambda e: e[2])
            point_tuples = [tuple(p) for p in points]
            uf = DSU(point_tuples)
            total_cost = 0
            edges_used = 0

            for u, v, w in edges:
                if uf.union(u, v): # if we were able to connect the two nodes that were previously not connected
                    total_cost += w
                    edges_used += 1
                    if edges_used == len(points) - 1:
                        break
            
            return total_cost
        
        return kruskals(edges)

class DSU:
    # initialization
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    # find algorithm with flattening
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    # union algorithm
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False # we don't need to join them
        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1 # always make sure root 2 is the smaller one
        
        self.parent[root2] = root1 # place root 2 under root 1
        if self.rank[root1] == self.rank[root2]: # if they are both the same rank
            self.rank[root1] += 1
        return True
    
    
