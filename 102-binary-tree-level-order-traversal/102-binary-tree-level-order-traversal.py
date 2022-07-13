# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        # BFS
        queue = deque([(1,root)])
        toRet = defaultdict(list)
        
        
        while queue:
            lvl, node = queue.popleft()
            
            # Do stuff with node
            toRet[lvl].append(node.val)
            
            
            # add children
            if(node.left):
                queue.append((lvl+1,node.left))
            if(node.right):
                queue.append((lvl+1,node.right))
        return toRet.values()
    
            
            
        
        