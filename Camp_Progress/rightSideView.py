# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using recursion (dfs)
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
    
# using iterative
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        queue = [root]
        ans = []
        
        while queue:
            cur_level = []
            length = len(queue)

            while length > 0:
                cur = queue.pop(0)
                cur_level.append(cur.val)
                length -= 1

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            ans.append(cur_level[-1])

        return ans