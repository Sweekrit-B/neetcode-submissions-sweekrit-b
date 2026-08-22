# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iteratively
        stack = [root]

        while stack:
            curr_node = stack.pop()
            if not curr_node:
                continue
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            stack += [curr_node.left, curr_node.right]
        
        return root