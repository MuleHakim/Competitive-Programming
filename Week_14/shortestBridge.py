class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid)
        
        def dfs(r,c):
            if inbound(r,c) and grid[r][c] and (r,c) not in visited:
                visited.add((r,c))
                directions = ((r,c+1),(r,c-1),(r+1,c),(r-1,c))
                for x,y in directions:
                    dfs(x,y)

        def bfs():
            ans = 0
            queue = deque(visited)
            while queue:
                count = len(queue)
                while count:
                    count -= 1
                    r,c = queue.popleft()
                    directions = ((r,c+1),(r,c-1),(r+1,c),(r-1,c))
                    for x,y in directions:
                        if inbound(x,y) and (x,y) not in visited:
                            if grid[x][y]: return ans
                            queue.append([x,y])
                            visited.add((x,y))
                ans += 1

        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()