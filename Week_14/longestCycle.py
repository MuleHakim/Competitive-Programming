class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        incoming = [0]*len(edges)
        for edge in edges:
            if edge != -1:
                incoming[edge] += 1

        visited = [0]*len(edges)
        queue = deque()
        for node in range(len(incoming)):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            visited[node] = 1
            neig = edges[node]
            if neig != -1:
                incoming[neig] -= 1
                if incoming[neig] == 0:
                    queue.append(neig)

        ans = -1
        for i in range(len(visited)):
            if not visited[i]:
                count = 1
                neig = edges[i]
                visited[i] = 1
                while neig != i:
                    visited[neig] = 1
                    count += 1
                    neig = edges[neig]
                ans = max(ans,count)

        return ans