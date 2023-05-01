class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(r,c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])

        ans = set()
        a,b = entrance
        queue = deque([(a,b,0)])
        maze[a][b] = "+"

        while queue:
            r, c, step = queue.popleft()
            a  = 0
            for i,j in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                if not inbound(i,j) and [r,c] != entrance: a += 1
                    
            if a >= 1: ans.add(step)

            directions = [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]
            for x,y in directions:
                if inbound(x,y) and maze[x][y] == ".":
                    maze[x][y] = "+"
                    queue.append((x,y,step+1))

        return min(ans) if ans else -1