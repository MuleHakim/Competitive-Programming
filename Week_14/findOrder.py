class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        queue = deque()
        order = []
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)
            for neig in graph[course]:
                incoming[neig] -= 1
                if incoming[neig] == 0:
                    queue.append(neig)

        if len(order) != numCourses:
            return []
        return order