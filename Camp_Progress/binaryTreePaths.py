# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        temp = []
        def dfs(node):
            if node:
                temp.append(str(node.val))
                if node.right == node.left:
                    ans.append("->".join(temp[:]))
                    temp.pop()
                    return
                
                dfs(node.left)
                dfs(node.right)
                temp.pop()
                
        dfs(root)
        return ans