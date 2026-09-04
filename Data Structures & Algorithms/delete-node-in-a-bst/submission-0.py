# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # how to delete a node: 
            # replace it with the right/left node
        
        if not root:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            successor = root.right
            while successor.left:
                successor = successor.left # find the minimum value on the right subtree to replace the current root value
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val) # delete the replacement node
        return root