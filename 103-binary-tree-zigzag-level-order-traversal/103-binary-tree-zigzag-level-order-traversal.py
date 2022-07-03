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
            levelVals = []
            
            # Process stuff on this level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    levelVals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if levelVals:
                res.append(levelVals if lev % 2 == 0 else levelVals[::-1])
            lev += 1
                
        return res
                
            
            
        