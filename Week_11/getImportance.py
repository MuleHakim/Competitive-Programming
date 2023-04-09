"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        value = defaultdict(int)
        
        for employee in employees:
            graph[employee.id] = employee.subordinates
            value[employee.id] = employee.importance

        def dfs(node,graph):
            self.total += value[node] 
            for neighbor in graph[node]:
                dfs(neighbor,graph)
                
        self.total = 0
        dfs(id,graph)
        return self.total