class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        outputArray = []

        for index1 in range(len(nums)):
            count = 0

            for index2 in range(len(nums)):
                if index1 != index2 and nums[index1] > nums[index2]:
                    count += 1

            outputArray.append(count)

        return outputArray

