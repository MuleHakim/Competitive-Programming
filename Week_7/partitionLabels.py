class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = { char: index  for index, char in enumerate(s)}
        listSizeParts = []
        maxIndex = 0
        indexPartition = 0
        for index, char in enumerate(s):
            maxIndex = max(last_index[char], maxIndex)
            if maxIndex == index:
                updatedIndex = index + 1 - indexPartition
                indexPartition += updatedIndex
                listSizeParts.append(updatedIndex)

        return listSizeParts
