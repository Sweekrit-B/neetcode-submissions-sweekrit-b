class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_dict = defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])
        
        all_nodes = set()

        def dfs(node, parent=None):
            if node in all_nodes: # if we have already added the node to the component
                return
            
            all_nodes.add(node)

            for connected in edge_dict[node]: # for each connection
                if connected == parent: # if we are re-adding the parent
                    continue
                dfs(connected, node) # add the current connected to the component
            
            return
        
        num_components = 0

        for num in range(n):
            # check if already in all_nodes
            if num in all_nodes:
                continue
            # call dfs
            dfs(num)
            # add a component
            num_components += 1

        return num_components
        

