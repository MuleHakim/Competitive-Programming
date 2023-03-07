# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(nodeP,nodeQ):
            if not nodeP and not nodeQ:
                return True
            if not nodeP or not nodeQ:
                return False
            if nodeP.val != nodeQ.val:
                return False

            return dfs(nodeP.right, nodeQ.right) and dfs(nodeP.left,nodeQ.left)
            
        return dfs(p,q)