class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.cur = []
        def backtrack(l):
            if len(self.cur) == k:
                self.ans.append(self.cur[:])
                return 

            for candidate in range(1, n + 1):
                if candidate in set(self.cur):
                    continue
                if self.cur and candidate <= self.cur[-1]:
                    continue
                self.cur.append(candidate)

                backtrack(l+1)
                self.cur.pop()

        backtrack(0)
        return self.ans