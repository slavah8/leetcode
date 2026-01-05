class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        

        primes = []

        def find_primes(n):

            is_prime = [True] * (n + 1)
            is_prime[0] = False
            is_prime[1] = False

            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for x in range(p * p, n + 1, p):
                        is_prime[x] = False
                p += 1
            
            return [i for i in range(2, n + 1) if is_prime[i]]
        
        primes = find_primes(n)
        primes = primes[:m]
        print(primes)
        INF = 10 ** 10
        # dp[x] defined as min number of prime numbers to sum up to x
        dp = [INF] * (n + 1)
        dp[0] = 0

        for x in range(1, n + 1):

            for p in primes:
                if p > x:
                    break
                
                dp[x] = min(dp[x], dp[x - p] + 1)
        
        return dp[n] if dp[n] != INF else -1


