class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        listTarget = []
        nums.sort()
        length = len(nums)

        for index in range(length):
            if nums[index] == target:
                listTarget.append(index)

        return listTarget
