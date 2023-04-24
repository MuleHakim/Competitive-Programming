class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in graph[node]:
                if color[neighbor] == color[node]: return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1-node_color):
                        return False

            return True
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        color = [-1] * (n+1)
        for i in range(1,n+1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                    
        return True