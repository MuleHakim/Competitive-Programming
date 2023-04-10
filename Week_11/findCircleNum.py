class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        ans = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] and i != j:
                    graph[i+1].append(j+1)
            if list(graph[i+1])==0:
                graph[i+1].append(i+1)

        visited = set()
        cities = list(graph.keys())
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        for num in cities:
            if num not in visited:
                visited.add(num)
                dfs(num)
                ans += 1

        return ans