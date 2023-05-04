class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        ans = []
        for word,count in counter.items():
            heapq.heappush(heap,(-count,word))
        while k > 0:
            count, word = heapq.heappop(heap)
            ans.append(word)
            k -= 1
        return ans