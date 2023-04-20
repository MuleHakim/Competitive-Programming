# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)

            self.ans = max(node.val + l + r, self.ans)
            return max(node.val + max(l, r), 0)
            
        self.ans = float("-inf")
        dfs(root)
        return self.ans