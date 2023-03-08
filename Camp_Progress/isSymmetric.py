# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(r1, r2):
              if not r1 or not r2:
                return r1 == r2

              return r1.val == r2.val and isSymmetric(r1.left, r2.right) and isSymmetric(r1.right, r2.left)

        return isSymmetric(root, root)