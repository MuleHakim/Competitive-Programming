class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()

        for i,j in edges:
            graph[i].append(j)
            indegree[j] += 1

        ans_dict = defaultdict(set)
        for i in range(n):
            if not indegree[i]:
                ans_dict[i] = {}
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neig in graph[node]:
                ans_dict[neig].add(node) 
                ans_dict[neig] = ans_dict[neig].union(ans_dict[node])
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    queue.append(neig)

        ans = []
        for i in range(n):
            ans.append(sorted(list(ans_dict[i])))

        return ans