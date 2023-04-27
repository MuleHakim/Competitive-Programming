# BFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited)==len(rooms)

# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(key):
            if key not in visited:
                visited.add(key)
                for room in rooms[key]:
                    dfs(room)
        dfs(0)
        return len(visited)==len(rooms)