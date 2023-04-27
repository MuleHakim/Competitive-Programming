# BFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for key,room in enumerate(rooms):
            graph[key] = room
        
        visited = set([0])
        queue = deque([0])
        while queue:
            room = queue.popleft()
            for key in graph[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return True if len(visited)==len(rooms) else False

# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for key,room in enumerate(rooms):
            graph[key] = room
            
        visited = set()
        def dfs(key):
            if key not in visited:
                visited.add(key)
                for room in graph[key]:
                    dfs(room)
        dfs(0)
        return True if len(visited)==len(rooms) else False