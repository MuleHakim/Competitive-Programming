from collections import defaultdict
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            count += 1
print(count//2)