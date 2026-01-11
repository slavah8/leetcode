class Solution:
    def encode(self, s: str) -> str:
        # dp[i][j] = the shortest encoded string for the substring s[i..j]

        n = len(s)

        dp = [[""] * n for _ in range(n)]
        # helper: return best repetition encoding for sub = s[i:j+1] if it helps else ""

        def repeat_encode(i, j):
            sub = s[i:j + 1]
            m = len(sub)

            # Find smallest period L where sub is made of repeats of sub[:L]
            for L in range(1, m // 2 + 1):
                if m % L != 0:
                    continue
                
                pattern = sub[:L] # exactly L characters
                if pattern * (m // L) == sub:
                    inner = dp[i][i + L - 1]
                    cand = f"{m // L}[{inner}]"
                    if len(cand) < m:
                        return cand
            return ""




        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                sub = s[i: j + 1]

                best = sub

                for k in range(i, j):
                    cand = dp[i][k] + dp[k + 1][j]
                    if len(cand) < len(best):
                        best = cand
                
                rep = repeat_encode(i, j)
                if rep and len(rep) < len(best):
                    best = rep
                
                dp[i][j] = best
        return dp[0][n - 1]