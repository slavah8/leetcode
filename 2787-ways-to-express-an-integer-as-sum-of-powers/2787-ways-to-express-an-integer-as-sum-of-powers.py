class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        

        vals = []
        i = 1
        while True:
            p = i ** x

            if p > n:
                break
            
            vals.append(p)
            i += 1
        
        print(vals)

        # dp[i][s] = number of ways to make sum s using only the first i values (vals[0..i-1])
        m = len(vals)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            v = vals[i - 1]

            for s in range(0, n + 1):
                # skip v
                dp[i][s] = dp[i - 1][s]

                # take v
                if s >= v:
                    dp[i][s] = (dp[i][s] + dp[i - 1][s - v]) % MOD
        
        return dp[m][n]