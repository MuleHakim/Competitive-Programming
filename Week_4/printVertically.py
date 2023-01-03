class Solution:
    def printVertically(self, s: str) -> List[str]:

        verticalOrder = []
        s = list(s.split())
        maxLen = 0

        for eachWord in s:
            maxLen = max(maxLen,len(eachWord))

        for pointer in range(len(s)):
            if len(s[pointer]) < maxLen:
                s[pointer] += " " * (maxLen - len(s[pointer]))

        length1 = maxLen
        length2 = len(s)

        for index1 in range(length1):
            eachVerticalOrder = s[0][index1]

            for index2 in range(1,length2):
                eachVerticalOrder += s[index2][index1]

            spaceIndex = len(eachVerticalOrder) - 1

            while eachVerticalOrder[spaceIndex] == " ":
                spaceIndex -= 1
            verticalOrder.append(eachVerticalOrder[:spaceIndex + 1])

        return verticalOrder
