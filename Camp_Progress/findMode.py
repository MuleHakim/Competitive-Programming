# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(node):
            if node:
                inOrder(node.left)
                self.stack.append(node.val)
                inOrder(node.right)

        self.stack = []
        self.ans = []
        inOrder(root)
        self.counter = Counter(self.stack)

        for val,count in self.counter.items():
            if count == max(self.counter.values()):
                self.ans.append(val)

        return self.ans