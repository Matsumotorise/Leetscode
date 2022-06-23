# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        cur = head = ListNode()
        ptr1, ptr2 = list1, list2
        
        
        while ptr1 and ptr2:
            if ptr1.val > ptr2.val:
                cur.next = ptr2
                cur = ptr2
                ptr2 = ptr2.next
            else:
                cur.next = ptr1
                cur = ptr1
                ptr1 = ptr1.next
                
                
        cur.next = ptr2 if ptr2 else ptr1
        
        return head.next
        
        
        
        