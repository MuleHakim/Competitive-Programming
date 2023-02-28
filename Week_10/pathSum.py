# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs1(node,path_sum):
            if node:
                path_sum += node.val
                if path_sum == targetSum:
                    self.count += 1
                dfs1(node.left,path_sum)
                dfs1(node.right,path_sum)

        def dfs2(node):
            if node:
                dfs1(node,0)
                path_sum = 0
                dfs2(node.left)
                dfs2(node.right)

        self.count = 0
        dfs2(root)
        return self.count