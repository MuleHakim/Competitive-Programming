class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for road in roads:
            i,j = road
            graph[i].add(j)
            graph[j].add(i)
        
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - (j in graph[i]))
        return ans