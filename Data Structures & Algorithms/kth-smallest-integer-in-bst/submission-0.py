# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def traverse(node, curr_pos):
            nonlocal res
            if not node or res is not None:
                return curr_pos
            
            curr_pos = traverse(node.left, curr_pos)
            if res is not None:
                return curr_pos
            curr_pos += 1
            if curr_pos == k:
                res = node.val
                return curr_pos
            
            curr_pos = traverse(node.right, curr_pos)
            return curr_pos
        
        traverse(root, 0)
        return res
