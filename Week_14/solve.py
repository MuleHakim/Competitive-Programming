class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfs(r,c):
            directions = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
            for x,y in directions:
                if inbound(x,y) and board[r][c] == "O" and (x,y) not in visited:
                    visited.add((x,y))
                    dfs(x,y)

        visited = set()
        visited.add((0,0))
        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][-1] == 'O':
                dfs(r, len(board)-1)

        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[-1][c] == 'O':
                dfs(len(board)-1, c)

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'