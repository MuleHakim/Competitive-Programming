class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles = sorted(piles,reverse=True)
        length = (len(piles) // 3) * 2
        maxNumCoins = 0

        for index in range(1,length,2):
            maxNumCoins += piles[index]

        return maxNumCoins

