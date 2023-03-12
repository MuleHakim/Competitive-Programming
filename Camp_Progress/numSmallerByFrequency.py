class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        n = len(words)
        for i in range(len(words)):
            counter = Counter(words[i])
            words[i] = counter[sorted(words[i])[0]]
            
        words.sort()
        for i in range(len(queries)): 
            counter = Counter(queries[i])
            temp = counter[sorted(queries[i])[0]]
            ans.append(n - bisect.bisect_right(words,temp))

        return ans