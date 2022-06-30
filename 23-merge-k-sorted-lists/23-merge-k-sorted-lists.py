# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda x, y: 1
        
        import heapq as hq
        heap = [(ptr.val, ptr) for ptr in lists if ptr]
        hq.heapify(heap) # O(k)
        dummy = ListNode()
        cur = dummy
        

        
        while heap: #(kn)
            val, ptr = heap[0]
            
            # Update heap as necessary
            if not ptr.next:
                hq.heappop(heap) # log(k)
            else:
                hq.heapreplace(heap, (ptr.next.val, ptr.next)) # O(log(k))
            
            # Update the chain
            cur.next = ptr
            cur = cur.next
                
                
        
        #O(knlog(k))
        return dummy.next
        
        
        
        
        
       