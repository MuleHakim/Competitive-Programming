class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSort(low,high):
            while low < high:
                mid = (low + high) // 2
                pivot_idx = max(min(low,mid),min(max(low,mid),high))
                nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
                pivot = nums[high]

                i = low - 1
                for j in range(low, high):
                    if nums[j] <= pivot:
                        i = i + 1
                        nums[i], nums[j] = nums[j], nums[i]

                nums[i + 1], nums[high] = nums[high], nums[i + 1]
                quickSort(low, i)
                quickSort(i+2, high)
                return

        quickSort(0,len(nums)-1)

        return nums[len(nums)-k]