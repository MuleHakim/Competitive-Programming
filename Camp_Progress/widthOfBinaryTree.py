# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root,1)]
        levelOrder = [1]

        while queue:
            cur_level = []
            length = len(queue)
            
            while length > 0:
                cur,num = queue.pop(0)
                cur_level.append(num)
                length -= 1
                if cur.left:
                    queue.append((cur.left,2*num))
                if cur.right:
                    queue.append((cur.right,2*num+1))
                    
            if len(cur_level) > 1:
                levelOrder.append(max(cur_level)- min(cur_level) + 1)
            else:
                levelOrder.append(1)

        return max(levelOrder)