class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bitwiseOR(path):
            tmp = 0
            for num in path:
                tmp |= num
            return tmp == maxXOR

        def backtrack(start,path):
            self.ans += bitwiseOR(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        self.ans = 0
        maxXOR = 0
        for num in nums:
            maxXOR |= num

        backtrack(0,[])

        return self.ans
