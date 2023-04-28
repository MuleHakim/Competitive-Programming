class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, par):
            count = 0
            for child in graph[node]:
                if child != par: 
                    count += dfs(child, node)
            return count + 2 if count or hasApple[node] else 0
            
        time = dfs(0, -1)        
        return max(0,time-2)