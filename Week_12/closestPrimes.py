class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right + 1)]
        is_prime[0] = is_prime[1] = False
        i = 2
        n = len(is_prime)
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1

        primes = [i for i in range(left, right + 1) if is_prime[i]]
        ans = []
        min_diff = math.inf
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < min_diff:
                min_diff = primes[i]- primes[i-1]
                ans = [primes[i-1], primes[i]]
        
        return ans if len(primes) > 1 else [-1,-1]