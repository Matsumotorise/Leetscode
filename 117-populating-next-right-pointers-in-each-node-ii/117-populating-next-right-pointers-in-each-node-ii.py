"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        from collections import deque
        
        queue = deque([root])
        
        while queue:
            prev = None
            for i in range(len(queue)):
                cur = queue.pop()
                if not prev:
                    prev = cur
                    if cur.left:
                        queue.appendleft(prev.left)
                    if cur.right:
                        queue.appendleft(prev.right)
                else:
                    prev.next = cur
                    if cur.left:
                        queue.appendleft(cur.left)
                    if cur.right:
                        queue.appendleft(cur.right)
                    
                    prev = cur
                    
                
                # add children
                
                
        return root
                
            