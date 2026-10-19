# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = 0
        for l in lists:
            # print(l)
            if l:
                heapq.heappush(min_heap, (l.val , counter, l))
                counter += 1
        
        head = ListNode(0)
        curr = head 
        while min_heap:
            val, _,  node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap,  (node.next.val, counter, node.next))
                counter += 1
            
            curr.next = node 
            curr = curr.next 
        
        return head.next 

                
        