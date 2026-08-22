# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        potential_starts = []
        
        def find_same_subroot(r_node):
            nonlocal potential_starts
            if not r_node:
                return
            
            if r_node.val == subRoot.val:
                potential_starts.append(r_node)
            find_same_subroot(r_node.left)
            find_same_subroot(r_node.right)

            return
        
        find_same_subroot(root)

        def same_tree_recurse(r_node, sr_node):
            if (r_node and not sr_node) or (sr_node and not r_node):
                return False
            if not r_node and not sr_node:
                return True
            if (r_node.val != sr_node.val):
                return False
            
            return same_tree_recurse(r_node.left, sr_node.left) and same_tree_recurse(r_node.right, sr_node.right)

        for start in potential_starts:
            if same_tree_recurse(start, subRoot):
                return True
        
        return False