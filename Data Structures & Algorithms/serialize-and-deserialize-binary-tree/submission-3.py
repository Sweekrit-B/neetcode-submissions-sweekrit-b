# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # preorder traversal
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialize = ""
        
        def dfs(node):
            nonlocal serialize
            if not node:
                serialize += "N,"
                return
            serialize += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        print(serialize)
        return serialize
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N,": return None
        q = deque(data.split(',')[:-1])
        root = TreeNode(q.popleft())
        
        def traverse(node):
            left = q.popleft()
            if left != 'N':
                left_node = TreeNode(left)
                node.left = left_node
                traverse(left_node)
            right = q.popleft()
            if right != 'N':
                right_node = TreeNode(right)
                node.right = right_node
                traverse(right_node)
        
        traverse(root)
        return root
            


                