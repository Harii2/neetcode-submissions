# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root: TreeNode):
            if not root:
                return 
            
            helper(root.left)
            helper(root.right)
            left_val = root.left
            root.left = root.right
            root.right = left_val 
        
        helper(root)
        return root
        