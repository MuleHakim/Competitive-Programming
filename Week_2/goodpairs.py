class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        result = 0
        counter = Counter(nums)

        for count in counter.values():

            while count > 1:
                
                result += count - 1
                count -= 1

        return result
