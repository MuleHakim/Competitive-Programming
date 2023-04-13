# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node.left and node.right:
                return str(node.val) + "(" + str(dfs(node.left)) +  ")" + "(" + str(dfs(node.right)) + ")" 
            if node.left:
                return str(node.val) + "(" + str(dfs(node.left)) +  ")"
            if node.right:
                return str(node.val) + "()" + "(" + str(dfs(node.right)) + ")"
            return str(node.val)
        return dfs(root)