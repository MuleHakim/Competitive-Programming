class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        controller = True
        if len(arr) < 3: return False
        if arr[1] < arr[0]: return False

        for i in range(1,len(arr)):

            if arr[i] == arr[i - 1]: return False

            if controller:
                if arr[i] < arr[i - 1]: controller = False

            if not controller:
                if arr[i] > arr[i - 1]: return False
                
        return controller == False
        
