class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left = []
        right = []
        equal = []

        for num in nums:

            if num < pivot:
                left.append(num)

            elif num > pivot:
                right.append(num)

            else:
                equal.append(num)

        return left + equal + right
