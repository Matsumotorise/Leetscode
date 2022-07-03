# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        queue = deque([root])
        res = []
        
        lev = 0
        
        while queue:
            levelVals = deque([])
            # Process stuff on this level
            for i in range(len(queue)):
                node = queue.popleft()
                # exit conditions
                if not node:
                    continue
                if lev % 2 == 0:
                    levelVals.append(node.val)
                else:
                    levelVals.appendleft(node.val)
                    
                queue.append(node.left)
                queue.append(node.right)
                
                
            res.append(levelVals)
            lev += 1
                
        res.pop()
                
        return res
                
            
            
        