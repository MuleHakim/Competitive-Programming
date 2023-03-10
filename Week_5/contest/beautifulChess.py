# Method 1
def beautifulChess():
    matrix = []
    for _ in range(8):
        arr = list(input().strip())
        matrix.append(arr)
    for i in range(6):
        if matrix[i].count("#") == 2 and matrix[i + 1].count("#") == 1 and matrix[i + 2].count("#"):
            row = i + 1
            col = matrix[i + 1].index("#")
            return str(row + 1) + " " + str(col + 1)
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        input()
        print(beautifulChess())

# Method 2
from collections import defaultdict
def beautifulChess(t):
    for _ in range(t):
        input()
        matrix = []
        dict_ = defaultdict(list)
        dict_2 = defaultdict(list)
 
        for _ in range(8):
            arr = list(input().strip())
            matrix.append(arr)
            
        for i in range(8):
            for j in range(8):
                if matrix[i][j] == '#':
                    dict_[j-i].append([i,j]) 
                    
        sortedValues = sorted(dict_, key=lambda k: len(dict_[k]), reverse=True)
        allDiag = []
        values = dict_[sortedValues[0]]
        allDiag += values
 
        for i in range(8):
            for j in range(8):
                if matrix[i][j] == '#':
                    dict_2[i+j].append([i,j])
                    
        sortedValues = sorted(dict_2, key=lambda k: len(dict_2[k]), reverse=True)
        values = dict_2[sortedValues[0]]
        allDiag += values

        ans = ""
        for val in allDiag:
            if allDiag.count(val) == 2:
                x, y = val
                ans = str(x + 1) + " " + str(y + 1)
                break
        print(ans)

if __name__ == '__main__':
    testCase = int(input())
    beautifulChess(testCase)
