from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)

def AddEdge(b,c):
    graph[b].append(c)
    graph[c].append(b)
def Vertex(u):
    temp = graph[u]
    print(*temp)

for _ in range(k):
    arr = list(map(int,input().split()))
    if len(arr) == 3:
        a,b,c = arr
        AddEdge(b,c)
    else:
        a,b = arr
        if graph[b]:
            Vertex(b)
        else:
            print()