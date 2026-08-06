# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            print(f"Looking at {root.val}")
            height_left = dfs(root.left)
            height_right = dfs(root.right)
            print(f"Number left: {height_left}, number right: {height_right}")
            if abs(height_right - height_left) > 1:
                flag = False
            print(f"Total height under {root.val}: {1 + max(height_left, height_right)}")
            return 1 + max(height_left, height_right)
        dfs(root)
        return flag