class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # use 10 bit bitmask for every prime number <= 30

        primes = [2,3,5,7,11,13,17,19,23,29]
        prime_index = {p: i for i, p in enumerate(primes)}
        SIZE = 1 << len(primes)
        cnt = [0] * 31
        for x in nums:
            cnt[x] += 1

        # Convert value v (2..30) into a prime-bitmask, or -1 if v has a squared prime factor
        def mask_of(v):
            m = 0
            for p in primes:
                if v % p == 0:
                    c = 0
                    while v % p == 0:
                        v = v // p
                        c += 1
                        if c > 1:
                            return -1
                    m |= 1 << prime_index[p]
            return m
        
        masks = [0] * 31
        for v in range(2, 31):
            masks[v] = mask_of(v)

        # dp[mask] = # ways to select indices from values 2..30 whose primes used are exactly the set mask
        dp = [0] * SIZE
        dp[0] = 1

        for v in range(2, 31):
            if cnt[v] == 0:
                continue
            
            mv = masks[v]
            if mv == -1:
                continue
            for mask in range(SIZE - 1, -1, -1):
                if (mask & mv) == 0:
                    dp[mask | mv] = (dp[mask | mv] + dp[mask] * cnt[v]) % MOD
        
        base = sum(dp[1:]) % MOD
        if cnt[1]:
            base = (base * pow(2, cnt[1], MOD)) % MOD
        return base

