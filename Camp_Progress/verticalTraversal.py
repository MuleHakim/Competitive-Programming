# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dic = defaultdict(list)
        
        def dfs (root, x = 0, y =0):
            if not root:
                return []
            
            left = dfs(root.left,x + 1, y - 1 )
            curr = [[root.val, (x, y)]]
            right = dfs(root.right, x + 1 , y + 1)
            
            return left + curr + right
        
        arr = dfs(root)
        arr.sort(key = lambda k :k[1][0])
        arr.sort(key = lambda k : k[1][1])
        
        res = []
        for val, tpl in arr:
            my_dic[tpl] += [val]
            if len(my_dic) > 1:
                my_dic[tpl].sort()

        temp = defaultdict(list)
        for key, val in my_dic.items():
            temp[key[1]] += val

        res = []
        for val in temp.values():
            res.append(val)
        return res