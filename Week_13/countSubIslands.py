class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        def inbound(row,col):
            return 0<=row<len(grid1) and 0<=col<len(grid1[0])
            
        def dfs(row,col,visited):
            if inbound(row,col) and (row,col) not in visited and grid2[row][col]:
                grid2[row][col] = 0
                visited.add((row,col))
                dfs(row+1,col,visited)
                dfs(row-1,col,visited)
                dfs(row,col+1,visited)
                dfs(row,col-1,visited)
        
        def isSubIsland(visited):
            for row, col in visited:
                if not grid1[row][col]:
                    return False
            return True

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col]:
                    visited = set()
                    dfs(row,col,visited)
                    if isSubIsland(visited):
                        count += 1

        return count