class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return 1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1)
            
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_area = max(max_area, area(r,c))
        return max_area