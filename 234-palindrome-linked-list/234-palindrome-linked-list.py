# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # revserse after slow
        
        prev = slow
        cur = slow.next
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        ptr1, ptr2 = head, prev
        
        while ptr1 and ptr2:
            print(ptr1.val, ptr2.val)
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True
        
            
            