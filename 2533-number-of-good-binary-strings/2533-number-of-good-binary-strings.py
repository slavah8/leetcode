class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[L] defined as number of good strings of exact length L
        dp = [0] * (maxLength + 1)

        dp[0] = 1

        for L in range(1, maxLength + 1):
            ways = 0
            if L - zeroGroup >= 0:
                ways += dp[L - zeroGroup]
            
            if L - oneGroup >= 0:
                ways += dp[L - oneGroup]
            
            dp[L] = ways % MOD
        
        ans = 0
        for l in range(minLength, maxLength + 1):
            ans = (ans + dp[l]) % MOD
        
        return ans
