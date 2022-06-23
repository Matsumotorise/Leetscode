# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minEle = min(p.val, q.val)
        maxEle = max(p.val, q.val)
        
        cur = root
        
        while cur:
            if cur.val < minEle:
                cur = cur.right
            elif cur.val > maxEle:
                cur = cur.left
            else:
                return cur
                
                
                
                
            
                
            
        
        
            
                
            
            
            

        
        
        
        