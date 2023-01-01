class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        totalE = sum(num for num in nums if i % 2 == 0)

        for value,index in queries:
            if nums[index] % 2 == 0:
                totalE -= nums[j]
            nums[index] += value

            if nums[index] % 2 == 0:
                totalE += nums[index]
            res.append(totalE)

        return res
