class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7

        def build_dp(C, maxL):
            dp = [0] * (maxL + 1)
            dp[0] = 1
            window = dp[0]

            for t in range(1, maxL + 1):
                dp[t] = window
                window = (window + dp[t]) % MOD
                if t - C >= 0:
                    window = (window - dp[t - C]) % MOD
            return dp
        
        runs = []
        i = 0
        N = len(pressedKeys)
        while i < N:
            j = i
            while j < N and pressedKeys[i] == pressedKeys[j]:
                j += 1
            runs.append((pressedKeys[i], j - i))
            i = j
        
        max_len = max(L for _, L in runs)
        f3 = build_dp(3, max_len)
        f4 = build_dp(4, max_len)

        ans = 1
        for digit, L in runs:
            if digit in ('7', '9'):
                ans = (ans * f4[L]) % MOD
            else:
                ans = (ans * f3[L]) % MOD
        return ans 