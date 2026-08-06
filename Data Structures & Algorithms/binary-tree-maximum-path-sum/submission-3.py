# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        def dfs(root):
            nonlocal maxPath
            # print(f"Looking at node: {root.val}")
            if not root.left and not root.right:
                # print(f"No children, returning {root.val}")
                maxPath = max(maxPath, root.val)
                return root.val
            left = float('-inf')
            right = float('-inf')
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            # print(f"Looking at node: {root.val} (second access)")
            # get the 5 possible sums
            root_and_left = root.val + left
            # print(f"Root and left: {root_and_left}")
            root_and_right = root.val + right
            # print(f"Root and right: {root_and_right}")
            root_and_both = root.val + left + right
            # print(f"Root and left and right: {root_and_both}")
            just_left = left
            # print(f"Left: {just_left}")
            just_right = right
            # print(f"Right: {just_right}")
            # maxPath is the maximum of all of these and the root
            maxPath = max(maxPath, root.val, root_and_left, root_and_right, root_and_both, just_left, just_right)
            # print(f"Max path: {maxPath}")
            # return value will have to be inclusive and only ONE of the paths
            maxInclusive = max(root.val, root_and_left, root_and_right)
            # print(f"Max inclusive: {maxInclusive}")
            return maxInclusive
        dfs(root)
        return maxPath