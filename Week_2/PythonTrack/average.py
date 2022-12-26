class Solution:
    def average(self, salary: List[int]) -> float:

        length = len(salary)
        minSalary = min(salary)
        maxSalary = max(salary)
        total = sum(salary)
        requiredTotal = total - minSalary - maxSalary
        
        return requiredTotal / (length-2)
