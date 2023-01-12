class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        numOfColDel = 0
        length1 = len(strs[0])
        length2 = len(strs)
        
        for index1 in range(length1):

            currChar = ord(strs[0][index1])
            for index2 in range(1,length2):

                if currChar > ord(strs[index2][index1]):
                    numOfColDel += 1
                    break
                else:
                    currChar = ord(strs[index2][index1])

        return numOfColDel
