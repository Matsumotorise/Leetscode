# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSumHelper(self, root: TreeNode, depth: int) -> int:
        
        if root == None:
            return 0, -1
        
        if root.left == None and root.right == None:
            return root.val, depth
        
        l, lDepth = self.deepestLeavesSumHelper(root.left, depth + 1)
        r, rDepth = self.deepestLeavesSumHelper(root.right, depth + 1)
        
        if(lDepth < rDepth):
            return r, rDepth;
        elif(rDepth < lDepth):
            return l, lDepth;
        
        return r + l, lDepth;
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.deepestLeavesSumHelper(root, 0)[0]
        