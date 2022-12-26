class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict_ = {}
        tmp = 96
        res = ""
        for i in range(1,27):
            if i > 9:
                dict_[str(i)+"#"] = chr(tmp+i)
            else:
                dict_[str(i)] = chr(tmp+i)
        i = 0
        while i<len(s):
            if i<len(s)-2 and s[i+2]=="#":
                res += dict_[s[i:i+3]]
                i += 3
            else:
                res += dict_[s[i]]
                i += 1
        return res
