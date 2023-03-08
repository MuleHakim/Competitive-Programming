# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,p):
            if node:
                if p.val < node.val:
                    self.common.append(node.val)
                    dfs(node.left,p)
                elif p.val > node.val:
                    self.common.append(node.val)
                    dfs(node.right,p)
                else:
                    self.common.append(node.val)
                return
                
        def dfs2(node,q):
            if node:
                if q.val < node.val:
                    self.common2.append(node.val)
                    dfs2(node.left,q)
                elif q.val > node.val:
                    self.common2.append(node.val)
                    dfs2(node.right,q)
                else:
                    self.common2.append(node.val)
                return

        self.common = []
        self.common2 = []
        
        dfs(root,p)
        dfs2(root,q)
        ans = 0
        length = min(self.common,self.common2)

        for i in range(len(self.common)):
            if self.common[i] in set(self.common2):
                ans = self.common[i]

        return TreeNode(ans)