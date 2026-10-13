"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        copy_map = {}
        curr = head 
        while curr:
            copy_map[curr] = Node(curr.val)
            curr = curr.next 
        
        curr = head 
        while curr:
            copy = copy_map[curr]
            copy.next = copy_map[curr.next] if curr.next else None 
            copy.random = copy_map[curr.random] if curr.random else None
            curr = curr.next
        
        return copy_map[head]