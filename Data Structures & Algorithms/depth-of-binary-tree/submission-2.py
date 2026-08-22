# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root: return 0

        def find_depth(node):
            if not node:
                return 0
            
            left_depth = find_depth(node.left)
            right_depth = find_depth(node.right)

            return max(left_depth, right_depth) + 1
        

        return find_depth(root)