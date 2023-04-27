class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        nums = [i for i in range(1, n+1)]

        def dfs(cur, nums, j):
            if len(cur) == n:
                self.ans += 1
                return
            for i in range(len(nums)):
                if nums[i] % j == 0 or j % nums[i] == 0:
                    dfs(cur + [nums[i]], nums[:i] + nums[i+1:], j-1)

        dfs([], nums, n)
        return self.ans