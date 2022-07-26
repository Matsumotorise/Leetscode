# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        maxS = 0
        
        while queue:
            s = 0
            curLen = len(queue)
            for _ in range(curLen):
                curNode = queue.popleft()
                s+=curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            maxS = s
        return maxS
            