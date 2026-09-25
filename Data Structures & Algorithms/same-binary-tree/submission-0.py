# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(
            p, q
        ):
            if not p and not q:
                return True 
            
            if not p:
                return False
            if not q:
                return False
            
            left_equal = helper(p.left, q.left)
            right_equal = helper(p.right, q.right)

            return left_equal and right_equal and p.val == q.val 
        
        return helper(p,q)
