# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return bst(node.right, node.val, high) and bst(node.left, low, node.val)
                   
        left_range = -math.inf
        right_range = math.inf

        return bst(root,left_range,right_range)