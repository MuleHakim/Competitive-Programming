class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 1
        for seeker in range(1,len(nums)):
            if nums[seeker] != nums[seeker - 1]:
                nums[holder] = nums[seeker]
                holder += 1
                
        return holder
