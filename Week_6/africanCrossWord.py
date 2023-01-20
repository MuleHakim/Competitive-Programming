# method 1
def africanCrossWord():
    n, m = list(map(int,input().rstrip().split()))
    grid = [list(input().rstrip()) for _ in range(n)]
    encrypted = ""

    def checkCol(col,curVal):
        colString = ""
        for i in range(n):
            colString += grid[i][col]

        return colString.count(curVal) == 1

    for i in range(n):
        for j in range(m):
            if grid[i].count(grid[i][j]) == 1 and checkCol(j,grid[i][j]):
                encrypted += grid[i][j]
                
    return encrypted
if __name__ == '__main__':
    print(africanCrossWord())

# method 2
#def africanCrossWord():
#    n, m = list(map(int,input().rstrip().split()))
#    grid = [list(input()) for _ in range(n)]
#    crossed = set()
#    encrypted = ""
# 
#    for i in range(n):
#        dictRow  = {}
#        for j in range(m):
#            if grid[i][j] in dictRow:
#                crossed.add(str(i)+"r"+grid[i][j])
#            else:
#                dictRow[grid[i][j]] = 1
# 
#    for i in range(m):
#        dictCol = {}
#        for j in range(n):
#            if grid[j][i] in dictCol:
#                crossed.add(str(i)+"c"+grid[j][i])
#            else:
#                dictCol[grid[j][i]] = 1
# 
#    for i in range(n):
#        for j in range(m):
#            if ((str(i) + "r" + grid[i][j]) not in crossed) and ((str(j) + "c" + grid[i][j]) not in crossed):
#                encrypted += grid[i][j]
#    return encrypted
#if __name__ == '__main__':
#    print(africanCrossWord())
