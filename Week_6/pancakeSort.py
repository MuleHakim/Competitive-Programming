class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        if arr == sorted(arr):
            return []

        output = []
        length = len(arr)

        for index in range(length):

            maxValue = max(arr[:length - index])
            maxIndex = arr.index(maxValue) + 1
            arr[:maxIndex] = arr[:maxIndex][::-1]
            output.append(maxIndex)

            arr[:length - index] = arr[:length - index][::-1]
            output.append(length - index)

        return output
