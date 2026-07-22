class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        edge_dict = defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])
        
        branch = set()
        done = set()

        def dfs(node, parent=None):
            if node in branch: # if there is a cycle
                return False
            
            branch.add(node)
            for connected in edge_dict[node]:
                if parent is not None:
                    if connected == parent:
                        continue
                if not dfs(connected, node):
                    return False
            
            branch.remove(node) # remove from current branch if everything checks out
            done.add(node) # add to the "done" set
            return True # return True by default
        
        if dfs(edges[0][0]):
            if len(done) == n:
                return True
        
        return False