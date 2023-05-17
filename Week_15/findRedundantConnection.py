class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def getRep(node):
            rep = arr[node]
            while rep != node:
                node = rep
                rep = arr[rep]
            return rep

        def union(x,y):
            rep_x = getRep(x)
            rep_y = getRep(y)
            if rep_x == rep_y:
                ans.append([x,y])
            else:   
                arr[rep_y] = rep_x

        n = len(edges)
        arr = [i for i in range(n+1)] 
        ans = []
        for i, j in edges:
            union(i,j)

        return ans[-1]
                