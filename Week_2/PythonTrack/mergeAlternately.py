class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        lengthWord1 = len(word1)
        lengthWord2 = len(word2)
        length = min(lengthWord1,lengthWord2)
        result = ""

        for i in range(length):
            result += word1[i] + word2[i]

        if lengthWord1 > lengthWord2:
            result += word1[length:]

        elif lengthWord2 > lengthWord1: 
            result += word2[length:]

        return result

