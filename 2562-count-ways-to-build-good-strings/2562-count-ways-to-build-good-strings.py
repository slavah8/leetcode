class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

        # dp[len] defined as number of ways to make string with exactly len
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for length in range(1, high + 1):

            # relation
            # can make string of length by using dp[length - zero] and dp[length - one]
            if length - zero >= 0:
                dp[length] += (dp[length - zero]) % MOD
            if length - one >= 0:
                dp[length] += (dp[length - one]) % MOD
            
        return sum(dp[length] for length in range(low, high + 1)) % MOD
                

 