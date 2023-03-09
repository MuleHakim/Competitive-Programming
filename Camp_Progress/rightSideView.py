# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node,level):
            if node:
                if len(self.ans) == level:
                    self.ans.append(node.val)

                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
                

        self.ans = []
        dfs(root,0)
        
        return self.ans