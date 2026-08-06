# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node):
            nonlocal max_diameter
            if not node.left and not node.right:
                return 0
            left_height = 0
            right_height = 0
            if node.left:
                left_height = 1 + dfs(node.left)
            if node.right:
                right_height = 1 + dfs(node.right)
            # check if the left height + right height is more than the current max
            max_diameter = max(max_diameter, left_height + right_height)
            # return the maximum of the two
            return max(left_height, right_height)
        dfs(root)
        return max_diameter