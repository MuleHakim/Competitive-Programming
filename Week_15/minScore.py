class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def getRep(node):
            if arr[node] != node:
                arr[node] = getRep(arr[node])

            return arr[node]

        def union(x,y):
            rep_x = getRep(x)
            rep_y = getRep(y)
            if rep_x != rep_y:
                arr[rep_y] = rep_x

        arr = [i for i in range(n+1)] 
        for i, j,dist in roads:
            union(i,j)
            
        ans = math.inf
        for i,j,dist in roads:
            if getRep(1) == getRep(j):
                ans = min(ans,dist)

        return ans