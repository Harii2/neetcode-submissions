"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        mapper = {}
        def helper(node):
            if not node:
                return 
            if node in mapper:
                return mapper[node]
            
            clone = Node(node.val)
            mapper[node] = clone
            
            for neigh in node.neighbors:
                clone.neighbors.append(
                    helper(
                        neigh
                    )
                )
            return clone 

        return helper(
            node
        )



        