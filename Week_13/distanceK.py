# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                graph[cur.val].append(cur.left.val)
                graph[cur.left.val].append(cur.val)
            if cur.right:
                queue.append(cur.right)
                graph[cur.val].append(cur.right.val)
                graph[cur.right.val].append(cur.val)

        visited = set([target.val])
        queue = deque([target.val])
        while queue and k:
            length = len(queue)
            while length:
                cur = queue.popleft()
                for neig in graph[cur]:
                    if neig not in visited:
                        queue.append(neig)
                        visited.add(neig)
                length -= 1
            k -= 1
            
        return list(queue)