# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def helper(root):
            nonlocal diameter
            if not root:
                return 0, 0 
            
            left_height, left_diameter = helper(
                root.left
            )
            right_height, right_diameter = helper(
                root.right
            )
            curr_diameter = left_height + right_height

            diamter = max(
                curr_diameter, 
                left_diameter,
                right_diameter
            )
            return 1+max(left_height,right_height) , diamter
        return helper(root)[1]
