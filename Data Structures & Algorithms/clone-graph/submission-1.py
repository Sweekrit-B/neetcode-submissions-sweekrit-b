"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        cloned = {}

        def dfs(curr_node):
            if curr_node in cloned:
                return cloned[curr_node]
            
            if curr_node == None:
                return
            
            copy = Node(curr_node.val)
            cloned[curr_node] = copy

            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)