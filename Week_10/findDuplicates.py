class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                while i < len(nums) and nums[i] == i + 1:
                    i += 1
  
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])

        return res