# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # observation about lowest common ancestor: always has p on left and q on right (or vice versa)

        def dfs(node):
            # if there is no node, you return nothing
            if not node:
                return (None, False, False)
            
            # at each node, check its left and right
            l_lca, l_contains_p, l_contains_q = dfs(node.left)
            r_lca, r_contains_p, r_contains_q = dfs(node.right)

            # check whether p and q are even children
            q_in_children = l_contains_q or r_contains_q
            p_in_children = l_contains_p or r_contains_p

            # if one of them contains p and q
            if l_contains_p and l_contains_q:
                return (l_lca, True, True)
            if r_contains_p and r_contains_q:
                return (r_lca, True, True)
            
            # if they each only contain one of the discrete values
            if (
                (l_contains_p and r_contains_q) or
                (l_contains_q and r_contains_p) or
                (node == p and q_in_children) or
                (node == q and p_in_children)
            ):
                return (node, True, True)
            
            # if they need to return that they have one value and don't have the other
            if (node == p and not q_in_children) or p_in_children:
                return (node, True, False)
            if (node == q and not p_in_children) or q_in_children:
                return (node, False, True)
            
            return (node, False, False)
            
        lca, _, _ = dfs(root)
        return lca
