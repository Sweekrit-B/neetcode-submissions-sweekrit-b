class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])
        
        branch = []
        done = set()
        cycle = set()

        def dfs(node, parent=None):
            if node in done:
                return
            if node in branch:
                print(f"Found {node}")
                cycle_nodes = branch[branch.index(node):]
                for i in range(len(cycle_nodes)):
                    cycle.add((cycle_nodes[i-1], cycle_nodes[i]))
                    cycle.add((cycle_nodes[i], cycle_nodes[i-1]))
                return

            branch.append(node)
            for connected in edge_dict[node]:
                if connected == parent:
                    continue
                dfs(connected, node)
            
            branch.pop()
            done.add(node)
            return
        
        dfs(1)
        print(cycle)
        
        for edge in edges[::-1]:
            if tuple(edge) in cycle:
                return edge