class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        result = ""
        spaceIndex = 0

        for index in range(len(s)):
            if index == spaces[spaceIndex]:
                result += " " + s[index]
                spaceIndex += 1
                if spaceIndex == len(spaces):
                    result += s[index + 1:]
                    break
            else:
                result += s[index]

        return result
