class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        operationDict = defaultdict(int)

        for index, num in enumerate(nums):
            operationDict[num] = index
            
        for x, y in operations:
            operationDict[y] = operationDict[x]
            del operationDict[x]

        sortedOperation = sorted(operationDict.items(), key=lambda x:x[1])

        return [key for key, value in sortedOperation]
