class Solution:
    def similarPairs(self, words: List[str]) -> int:

        result = 0
        length = len(words)
        for pointer1 in range(length - 1):
            for pointer2 in range(pointer1 + 1, length):
                if set(words[pointer1]) == set(words[pointer2]):
                    result += 1
                    
        return result
