class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(r,c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    queue.append((i,j))
                else:
                    mat[i][j] = "*"

        while queue:
            r,c = queue.popleft()
            directions = ((r,c+1),(r,c-1),(r+1,c),(r-1,c))
            for x,y in directions:
                if inbound(x,y) and mat[x][y] == "*":
                    mat[x][y] = mat[r][c] + 1
                    queue.append((x,y))
                    
        return mat