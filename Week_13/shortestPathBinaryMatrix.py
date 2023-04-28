class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(x,y):
            return 0 <= x < n and 0 <= y < n
            
        n = len(grid)
        if grid[0][0] or grid[-1][-1]: return -1
        queue = deque([(0,0,1)])
        grid[0][0] = 1
        while queue:
            row,col,dist = queue.popleft()
            if row == col == n-1:
                return dist
            directions = [(row+1,col),(row-1,col),(row,col-1),(row,col+1),(row+1,col+1),\
                       (row+1,col-1),(row-1,col-1),(row-1,col+1)]
            for x,y in directions:
                if inbound(x,y) and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x,y,dist+1))
        return -1