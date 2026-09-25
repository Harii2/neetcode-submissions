# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        bfs_array = []
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(
                    node.val
                )
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfs_array.append(
                values
            )
        right_side_view = []
        for level_order in bfs_array:
            right_side_view.append(
                level_order[-1]
            )
        return right_side_view

        