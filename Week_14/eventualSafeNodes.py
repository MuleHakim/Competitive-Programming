class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        adj_list = defaultdict(list)

        for node in range(len(graph)):
            for neig in graph[node]:
                adj_list[neig].append(node)
                indegree[node] += 1

        queue = deque()
        for node in range(len(graph)):
            if indegree[node] == 0:
                queue.append(node)

        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)

            for neig in adj_list[node]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    queue.append(neig)

        return sorted(ans)