class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        length = len(nums)
        arrangedArray = [0] * length

        index = 0
        evenIndex = 0
        oddIndex = 1

        while index < length:

            if nums[index] > 0:
                arrangedArray[evenIndex] = nums[index]
                evenIndex += 2

            else:
                arrangedArray[oddIndex] = nums[index]
                oddIndex += 2

            index += 1
                
        return arrangedArray
