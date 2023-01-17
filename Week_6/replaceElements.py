class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        length = len(arr)
        resArray = [0] * length
        greater = 0
        
        for index in range(length - 1, -1, -1):
            tmp = arr[index]
            greater = max(greater, tmp)
            resArray[index - 1] = greater

        resArray[-1] = -1

        return resArray
