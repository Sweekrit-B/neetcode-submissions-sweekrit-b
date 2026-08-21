# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS, keep track of the max of a branch
        
        good_nodes = 0

        def dfs(node, max_so_far):
            nonlocal good_nodes

            if not node:
                return
            if node.val >= max_so_far:
                good_nodes += 1
            
            new_max = max(node.val, max_so_far)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

            return
        
        dfs(root, root.val)
        return good_nodes