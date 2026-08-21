# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            curr_len = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if i == curr_len:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res            