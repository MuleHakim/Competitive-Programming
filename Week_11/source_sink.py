n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
sink = []
source = []
for i in range(n):
    for j in range(n):
        if graph[j][i]:
            break
    else:
        source.append(i + 1)

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            break
    else:
        sink.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)