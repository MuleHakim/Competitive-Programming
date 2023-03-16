class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(idx, prev, split):
            if idx >= len(s):
                return split >= 2
            for i in range(idx,len(s)):
                cur = int(s[idx:i+1])
                if (prev == "" or prev - cur == 1) and dfs(i+1, cur, split + 1):
                    return True
            return False

        return dfs(0,"",0)