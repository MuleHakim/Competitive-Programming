class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j: continue
                dist = abs(bombs[i][0] - bombs[j][0])**2 + abs(bombs[i][1] - bombs[j][1])**2
                if bombs[i][2]**2 >= dist:
                    graph[i] += [j]
        
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)
                    
        ans = 0
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans