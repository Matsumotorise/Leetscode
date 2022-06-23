# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxDepth = 0
        if not root:
            return maxDepth
        # DFS
        stack = [(root, 1)]
        
        
        while stack:
            # pop ele
            curNode, curDepth = stack.pop()
            maxDepth = max(maxDepth, curDepth)
            
            
            # append children
            if curNode.left:
                stack.append((curNode.left, curDepth + 1))
            if curNode.right:
                stack.append((curNode.right, curDepth + 1))
            
            
        return maxDepth
        
        
        