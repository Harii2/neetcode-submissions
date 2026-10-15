# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(root):
            if not root:
                result.append("null")
                return 
            result.append(
                str(root.val)
            )
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = data.split(",")
        preorder_index = 0 

        def construct():
            nonlocal preorder_index
            current_val  = result[preorder_index]
            if current_val == "null":
                preorder_index += 1 
                return None 
            
            node = TreeNode(
                val = int(current_val)
            )
            preorder_index += 1
            node.left = construct()
            node.right = construct()
            return node 
        
        return construct()
