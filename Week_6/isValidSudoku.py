class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for index1 in range(9):
            
            for index2 in range(9):

                cur = board[index1][index2]
                if cur != '.':

                    if cur + 'row ' + str(index1) in seen or \
                        cur + 'col ' + str(index2) in seen or \
                        cur + 'box ' + str(index1 // 3) + str(index2 // 3) in seen:
                        return False

                    seen.add(cur + 'row ' + str(index1))
                    seen.add(cur + 'col ' + str(index2))
                    seen.add(cur + 'box ' + str(index1 // 3) + str(index2 // 3))

        return True

