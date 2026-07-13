"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        cloned = {}

        def dfs(curr_node):
            # check if the current node is already in the mapping of the og graph to the new one
            if curr_node in cloned:
                return cloned[curr_node]

            # create an initial copy and assign it
            copy = Node(curr_node.val)
            cloned[curr_node] = copy

            # for each neighbor, first build out the node in it's entirety and then assign it
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            # by default, return the copy node
            return copy

        return dfs(node) if node else None
