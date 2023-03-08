# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.elements = 1
        self.total = 0
        self.res = 0

        def dfs(node):
            
            if node:
                self.total += node.val

                if node.left and node.right:
                    dfs(node.left)
                    dfs(node.right)
                    self.elements += 2

                elif node.left:
                    dfs(node.left)
                    self.elements += 1
                    
                elif node.right:
                    dfs(node.right)
                    self.elements += 1 
                
                return [self.elements, self.total]

        def helper(root):

            if root:
                temp = dfs(root)
                if temp[1] // temp[0] == root.val:
                    self.res += 1

                self.total = 0
                self.elements = 1
                helper(root.left)
                helper(root.right)

        self.res = 0
        helper(root)

        return self.res