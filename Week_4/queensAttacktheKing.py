class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        def isInBoard(x,y):
            if 0 <= x <= 7 and 0 <= y <= 7:
                return True
            return False

        def isQueen(x,y):
            for queen in queens:
                if queen == [x,y]:
                    return True
            return False

        directions = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
        queenAttackKing = []

        for dx, dy in directions:
            x, y = king

            while isInBoard(x,y):
                if isQueen(x,y):
                    queenAttackKing.append([x,y])
                    break

                x += dx
                y += dy

        return queenAttackKing
                
