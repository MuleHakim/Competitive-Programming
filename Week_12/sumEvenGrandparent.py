# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, par, g_par):
            if not node: return 0
            ans = 0
            if g_par == 0:
                ans += node.val
            ans += dfs(node.left, node.val % 2, par)
            ans += dfs(node.right, node.val % 2, par)
            return ans 
        return dfs(root, 1, 1)