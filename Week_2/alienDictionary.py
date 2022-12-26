class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        length = len(words)
        orderDict = defaultdict(int)

        for index, value in enumerate(order):
            orderDict[value] = index

        for index1 in range(length - 1):

            for index2 in range(index1, len(words[index1])):

                if words[index1] in words[index1 + 1]:
                    break

                if words[index1 + 1] in words[index1]:
                    return False

                if orderDict[words[index1][index2]] > orderDict[words[index1 + 1][index2]]:
                    return False

                elif orderDict[words[index1][index2]] == orderDict[words[index1 + 1][index2]]:
                    continue
                    
                else:
                    break

        return True
