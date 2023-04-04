class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        count = Counter(deck).values()
        return reduce(gcd, count) > 1