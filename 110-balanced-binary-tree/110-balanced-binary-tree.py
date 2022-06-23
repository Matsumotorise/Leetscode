# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Returns either depth of subtree or -1 if violation found
        def getDepth(root):
            if not root:
                return 0
            
            # Check left and right subtrees for depth
            lDepth, rDepth = getDepth(root.left), getDepth(root.right)
            
            if lDepth == -1 or rDepth == -1 or abs(rDepth - lDepth) > 1:
                return -1
            
            return max(lDepth, rDepth) + 1
        
        return True if getDepth(root) != -1 else False
            
            
            
            
        
        
        