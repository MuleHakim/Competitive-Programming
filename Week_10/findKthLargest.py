class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def median(low,mid,high):
            first, mid, last = nums[low], nums[mid], nums[high]
            if first <= mid <= last or last <= mid <= first:
                pivot = mid
                pivot_index = (low + high) // 2
            elif mid <= first <= last or last <= first <= mid:
                pivot = first
                pivot_index = low
            else:
                pivot = last
                pivot_index = high
            return pivot,pivot_index

        def quickSort(low,high):
            while low < high:
                mid = (low + high) // 2
                pivot,pivot_index = median(low,mid,high)
                nums[pivot_index], nums[high] = nums[high], nums[pivot_index]

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