class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(s, prev):

            if int(s) == prev - 1:
                return True

            for i in range(1, len(s)+1):
                cur = int(s[:i])
                if cur == prev - 1 and backtrack(s[i:], cur):
                    return True
                
            return False
        
        for i in range(1, len(s)):
            if backtrack(s[i:], int(s[:i])):
                return True

        return False