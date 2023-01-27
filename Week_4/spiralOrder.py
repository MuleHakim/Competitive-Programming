class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row, col = 0, 0
        totalItems = len(matrix) * len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # set initial direction to the right
        dx, dy = 0, 1
        visited = set()
        spiralOrder = []
        count = 0
        def onBoard(row, col):
           return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        while len(spiralOrder) != totalItems:
            spiralOrder.append(matrix[row][col])
            visited.add((row,col))
            if not onBoard(row + dx, col + dy) or (row + dx, col + dy) in visited:
                count +=1
                dx, dy = directions[count % 4]
            row += dx
            col += dy

        return spiralOrder

