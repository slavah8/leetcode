class Solution:
    def knightDialer(self, digits: int) -> int:
        
        MOD = 10 ** 9 + 7

        # dp[i] defined as number of distinct phone numbers of length n we can dial

        

        # if we start at 1 then we can jump to 6 and 8 
        # if we start at 2 we can jump to 7 and 9
        # if we start at 3 we can jump to 4 and 8
        # if we start at 4 we cna jumpo to 4 and 9
        # if we start at 6 we can jump to 0 and 1 and 7
        # if we start at 7 we can jump to 2 and 6
        # if we start at 8 we can jump to 1 and 8
        # if we start at 9 we can jump to 2 and 4

        # f(n, d) where n is the number of digits to dial and d is the current digit dialed.
        @lru_cache(None)
        def f(n, d):
            if n == digits - 1:
                return 1

            if d == 0:
                return (f(n + 1, 4) + f(n + 1, 6)) % MOD
            
            elif d == 1:
                return (f(n + 1, 6) + f(n + 1, 8)) % MOD
            
            elif d == 2:
                return (f(n + 1, 7) + f(n + 1, 9)) % MOD
            
            elif d == 3:
                return (f(n + 1, 4) + f(n + 1, 8)) % MOD
            
            elif d == 4:
                return (f(n + 1, 9) + f(n + 1, 3) + f(n + 1, 0)) % MOD
            
            elif d == 5:
                return 0
            
            elif d == 6:
                return (f(n + 1, 7) + f(n + 1, 0) + f(n + 1, 1)) % MOD
            
            elif d == 7:
                return (f(n + 1, 2) + f(n + 1, 6)) % MOD
            
            elif d == 8:
                return (f(n + 1, 1) + f(n + 1, 3)) % MOD
            
            elif d == 9:
                return (f(n + 1, 2) + f(n + 1, 4)) % MOD
            
        
        total = 0
        for d in range(0, 10):
            total = (total + f(0, d)) % MOD
        return total % MOD
            

