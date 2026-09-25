# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isBalancedTree(
        self, p, q
    ):
        if not p and not q:
            return True 
        if not p:
            return False
        if not q:
            return False
        
        left_balanced = self.isBalancedTree(
            p.left, q.left
        )
        right_balanced = self.isBalancedTree(
            p.right, q.right
        )
        return left_balanced and right_balanced and p.val == q.val

    def dfs(self, p, queue):
        if not p:
            return 
        self.dfs(p.left, queue)
        self.dfs(p.right, queue)
        queue.append(p)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isBalancedTree(
            root, subRoot
        ):
            return True
        return self.isSubtree(
            root.left, subRoot
        ) or self.isSubtree(
            root.right, subRoot
        )

        