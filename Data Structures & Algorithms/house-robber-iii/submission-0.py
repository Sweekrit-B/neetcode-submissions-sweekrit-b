# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # DFS/DP solution
        # at any given point, we want the sum inclusive and exclusive of the node
        # take example 2
            # say we are at node with value 3 -> max sum inclusive = 3, max sum exclusive = 6
            # next, we take node 5 -> max sum inclusive = 5, max sum exclusive = 0
            # next we take node 2 -> max sum inclusive = max sum exclusive of both children + node = 8, max sum exclusive = sum of maxes of both subtrees (as it doesnt matter) = 11
            # finally, we take node 1 -> max sum inclusive = max sum exclusive + node = 12, max sum exclusive = sum of maxes of both subtrees = 11
        
        def recurse(node):
            if not node:
                return (0, 0) # max sum inclusive, max sum exclusive
            left_subtree = recurse(node.left)
            right_subtree = recurse(node.right)
            max_inclusive = left_subtree[1] + right_subtree[1] + node.val
            max_exclusive = max(left_subtree) + max(right_subtree)
            return (max_inclusive, max_exclusive)
        
        return max(recurse(root))


                
