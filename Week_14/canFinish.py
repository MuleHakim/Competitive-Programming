class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        queue = deque()
        count = 0
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            count += 1
            for neig in graph[course]:
                incoming[neig] -= 1
                if incoming[neig] == 0:
                    queue.append(neig)

        return count != numCourses