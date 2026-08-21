# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for any given node, track the left and right bound

        def dfs(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False

            if not dfs(node.left, left, node.val) or not dfs(node.right, node.val, right):
                return False
            
            return True
        
        return dfs(root, float('-inf'), float('inf'))