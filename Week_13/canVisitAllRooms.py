class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,room in enumerate(rooms):
            graph[i] = room
            
        visited = set()
        def dfs(key):
            if key not in visited:
                visited.add(key)
                for room in graph[key]:
                    dfs(room)
        dfs(0)
        return True if len(visited)==len(rooms) else False