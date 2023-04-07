from collections import defaultdict
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
graph = defaultdict(list)
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            graph[i+1].append(j+1)
    temp = [len(graph[i+1])] + graph[i+1]
    print(*temp)