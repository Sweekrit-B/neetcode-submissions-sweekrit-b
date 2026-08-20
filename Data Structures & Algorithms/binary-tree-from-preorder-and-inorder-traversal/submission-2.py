# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # two facts: 
        # 1) preorder: first value is the root, second value is the root of the subtree (first val after removal) -> you will never go to the right without first going through everything in left
        # 2) inorder: every value to the left of the root is in the left subtree, everything to the right is in the right subtree
            # this can be used to partition the rest of the preorder array
        
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None # if the indices are not valid
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            # build left first since we need to move preorder
            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)

            return root
        
        return build(0, len(inorder) - 1)