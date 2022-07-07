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
        # Make copy of list node wise and attach pointers to the new nodes
        
        dummyNode = Node(1)
        
        dumCurNode = dummyNode
        curNode = head
        while curNode:
            dumCurNode.next = Node(x=curNode.val)
            dumCurNode = dumCurNode.next
            curNode.ref = dumCurNode
            curNode = curNode.next
            
            
        curNode = head
        dumCurNode = dummyNode
        while curNode:
            dumCurNode = dumCurNode.next
            if curNode.random:
                dumCurNode.random = curNode.random.ref
            curNode = curNode.next
            
            
            
        return dummyNode.next
        