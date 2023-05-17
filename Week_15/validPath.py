class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        arr = [i for i in range(n)]
        def getRep(node):
            rep = arr[node]
            while rep != node:
                node = rep
                rep = arr[rep]
            return rep

        def union(x,y):
            rep_x = getRep(x)
            rep_y = getRep(y)

            arr[rep_y] = rep_x
            
        for i, j in edges:
            union(i,j)

        return getRep(source) == getRep(destination)