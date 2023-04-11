# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if node:
                path += str(node.val)
                dfs(node.left, path)
                dfs(node.right, path)
                if node.left == node.right:
                    self.res += int(path)

        self.res = 0
        dfs(root,"")
        
        return self.res