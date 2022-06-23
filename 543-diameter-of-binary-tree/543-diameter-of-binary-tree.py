# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longestPath = 0
        
        # returns longest path
        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # 3 cases, include leftsubtree yourself then rightsubtree
            # Include left and something above you
            # Include right and something above you
            retVal = 1 + max(leftMax, rightMax)
            self.longestPath = max(self.longestPath, 1+leftMax+rightMax)
            return retVal
        
        dfs(root)
        
        return self.longestPath-1
            
            
            
            
            
        
        
        
        
        
        