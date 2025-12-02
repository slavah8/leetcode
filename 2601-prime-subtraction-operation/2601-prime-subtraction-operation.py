class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        MAXV = 1000
        n = len(nums)
        is_prime = [True] * (MAXV + 1)
        is_prime[0] = False
        is_prime[1] = False

        for x in range(2, int(MAXV ** 0.5) + 1):
            if is_prime[x]:
                step = x * x
                while step <= MAXV:
                    is_prime[step] = False
                    step += x
        primes = [i for i in range(2, 1001) if is_prime[i]]
        print(primes)

        INF = 10 ** 10
        prev = -INF

        for x in nums:

            best = INF
            if x > prev:
                best = x
            
            for p in primes:
                if p >= x:
                    break
                cand = x - p
                if cand > prev:
                    best = cand
            
            if best == INF:
                return False
            
            prev = best
        return True
        
