class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i,j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)

        node = -1
        for key in graph.keys():
            if len(graph[key]) == 1:
                node = key
                break

        visited = set()
        ans = []
        def dfs(node):
            if node not in visited:
                visited.add(node)
                ans.append(node)
                for neig in graph[node]:
                    dfs(neig)

        dfs(node)
        
        return ans