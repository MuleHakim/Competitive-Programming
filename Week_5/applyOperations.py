class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        length = len(nums)
        for index in range(1,length):
            if nums[index - 1] == nums[index]:
                nums[index - 1] *= 2
                nums[index] = 0

        write = 0
        read = 0
        while read < length:
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]

                write = write + 1
            read = read + 1

        return nums
