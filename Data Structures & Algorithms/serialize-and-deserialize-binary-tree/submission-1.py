# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = ""
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node:
                    serialized += str(curr_node.val) + ','
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
                else:
                    serialized += "N,"
        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N,": return None
        root = TreeNode(data[0])
        
        q = deque(data[1:].split(',')[1:-1])
        valid_nodes = deque([root])
        print(q)
        print(valid_nodes)
        
        while q:
            for i in range(len(valid_nodes)):
                curr_node = valid_nodes.popleft()
                left = q.popleft()
                right = q.popleft()
                if left != 'N':
                    left_node = TreeNode(int(left))
                    curr_node.left = left_node
                    valid_nodes.append(left_node)
                if right != 'N':
                    right_node = TreeNode(int(right))
                    curr_node.right = right_node
                    valid_nodes.append(right_node)
        
        return root