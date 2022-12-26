class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        tmp = ""
        res = tmp
        for j in range(len(strs[0])):
            tmp = strs[0][i:j+1]
            for k in range(len(strs)):
                if tmp not in strs[k][i:j+1]:
                    return res
            res = tmp
        return res
