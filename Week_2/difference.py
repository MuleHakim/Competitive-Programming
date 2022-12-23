class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if s=="":
            return t

        s = sorted(s)
        t = sorted(t)

        s_list = list(s)
        t = list(t)
        i = 0
        j = len(t)-1

        while i<j:

            if t[i] not in s_list:
                return t[i]
                
            if t[i] in s_list:
                s_list.pop(i)
                t.pop(i)
                j -= 1

        return t[i]
