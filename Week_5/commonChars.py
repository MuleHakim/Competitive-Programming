class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        commonCharatersList = []
        commonCount = [math.inf] * 26
        offset = ord("a")
        
        for word in words:
            count = [0] * 26
            
            for char in word:
                asci = ord(char)
                count[asci - offset] += 1

            for index in range(26):
                commonCount[index] = min(commonCount[index], count[index])

        countOfCommonChar = 26 - commonCount.count(0)
        count = 0

        for index in range(len(commonCount)):
            if commonCount[index] != 0:
                count += 1
                for _ in range(commonCount[index]):
                    commonChar = chr(index + offset)
                    commonCharatersList.append(commonChar)

            if count == countOfCommonChar: break

        return commonCharatersList
