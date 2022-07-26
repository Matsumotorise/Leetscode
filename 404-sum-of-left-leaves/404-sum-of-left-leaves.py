# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node=root):
            return ((dfs(node.right) if node.right else 0) + 
                   ( (dfs(node.left) if (node.left.left or node.left.right) else node.left.val) if node.left else 0))
        return dfs(root)
        