class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = [""]
        ans = 0
        for word in arr:
            for r in results:
                new_res = r+word
                if len(new_res) != len(set(new_res)): continue
                results.append(new_res)
                ans = max(ans, len(new_res))

        return ans
# Backtracking    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.backtrack(arr, '', 0)
        return self.ans

    def backtrack(self, arr, word, index):
        if len(word) != len(set(word)): return
        self.ans = max(self.ans, len(word))
        if index == len(arr):
            return
        for i in range(index, len(arr)):
            self.backtrack(arr, word+arr[i], i+1)