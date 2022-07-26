# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node=root):
            s = 0
            if node.left:
                if not node.left.left and not node.left.right:
                    s += node.left.val
                else:
                    s += dfs(node.left)
            if node.right:
                s += dfs(node.right)
            return s
        return dfs(root)
        