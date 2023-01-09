class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = []
        length = len(boxes)

        for index1 in range(length):
            numOfOpe = 0

            for index2 in range(length):
                if boxes[index2] == "0" or index1 == index2:
                    continue
                else:
                    numOfOpe += abs(index1 - index2)

            answer.append(numOfOpe)
            
        return answer

