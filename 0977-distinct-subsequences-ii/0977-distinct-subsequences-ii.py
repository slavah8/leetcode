class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        last = [-1] * 26
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        
        for i, char in enumerate(s, 1):
            c = ord(char) - ord('a')
            dp[i] = dp[i - 1] * 2
            if last[c] != -1:
                dp[i] = (dp[i] - dp[last[c] - 1]) % MOD
            last[c] = i
        return (dp[N] - 1) % MOD
